from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from password_reset.views import Recover, RecoverDone, Reset, ResetDone

from jobseeker.models import Profile
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, redirect_to_login
from django.http.response import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .forms import (
    CompanySignUpForm,
    LoginForm,
    JobseekrForm,

    UpdateUserForm,
    UsersPasswordRecoveryForm,
    UsersPasswordResetForm,
)
from django.shortcuts import redirect
from company.models import Company, Job


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'error_404.html', data)


def home_page(request):
    us = Profile.objects.all()
    
    job_post = Job.objects.all()

    context = {'us': us, 'job_post': job_post}
    return render(request, 'homepage.html', context)


class RecoverView(Recover):
    template_name = "account/recover.html"
    form_class = UsersPasswordRecoveryForm
    success_url_name = "recover_password_sent"
    email_template_name = "account/recover_email.txt"
    search_fields = ["username", "email"]


class RecoverDoneView(RecoverDone):
    template_name = "account/recover.html"


class RecoverResetView(Reset):
    template_name = "account/reset.html"
    success_url = "recover_password_done"
    form_class = UsersPasswordResetForm
    token_expires = 3600 * 2


class RecoverResetDoneView(ResetDone):
    template_name = "account/reset_done.html"


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = "account/create.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # form.instance.roles.set('2')

        user = form.save()
        login(self.request, user)
        return redirect('/')


class JobseekerUserView(CreateView):
    model = User
    form_class = JobseekrForm
    template_name = "account/create.html"
    redirect_to_login = ("homepage")
    authenticated_redirect_url = reverse_lazy("homepage")
    msg = _(
        'Your account has been successfully created, access <a href="{0}">'
        "this page</a> and register the pet :)"
    )

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
        return super().get_context_data(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(resolve_url(self.authenticated_redirect_url))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)
        return redirect('/')

    # def form_valid(self, form):
    #     form.instance = True
    #     return super(CreateUserView, self).form_valid(form)

    def get_success_url(self):

        url = reverse("homepage")
        messages.success(self.request, self.msg.format(url))
        user = authenticate(
            username=self.request.POST.get("username"), password=self.request.POST.get("password1")
        )
        login(self.request, user)

        return reverse("homepage")


class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "account/edit_profile.html"
    model = User
    form_class = UpdateUserForm

    def get_success_url(self):
        messages.success(self.request, _("Changes saved successfully."))
        return reverse("homepage")

    def get_object(self, queryset=None):
        return self.request.user


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "account/edit_profile.html"
    model = Profile
    form_class = UpdateUserForm

    def get_success_url(self):
        messages.success(self.request, _("Changes saved successfully."))
        return reverse("homepage")

    def get_object(self, queryset=None):
        return self.request.user

    def save(self, *args, **kwargs):

        # Call the real save() method
        super(Profile, self).save(*args, **kwargs)


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"


class UserProfileView(TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["object"] = a = self.request.user

        return context


# class ProfileDetailView(DetailView):
#     template_name = "account/profile.html"
#     model = OwnerProfile

#     def get_context_data(self, **kwargs):
#         context = super(ProfileDetailView, self).get_context_data(**kwargs)
#         context["o"] = self.object.pet_set.all()
#         return context


def confirm_information(request):
    """This check that the user has confirmed the information and
    redirect to the correct view"""
    if request.user:
        if request.user.is_information_confirmed:
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return HttpResponseRedirect(reverse("edit"))

# def RegisterEdit(request):

#     if request.user:
#         userid = request.user
#         print(userid)
#       # obj = get_object_or_404(Profile, user =userid )
#     # print(obj)
#     if request.method == 'POST':
#         form = ProfileEdit(request.POST or None)
#         form.instance.user=userid
#         if form.is_valid():
#             form.save()
#             return HttpResponse('home')
#         else:

#             form = ProfileEdit(request.POST or None, instance = request.user)


#     else:
#         form = ProfileEdit(request.POST or None)
#     return render(request, 'account/edit_profile.html', {'form': form})
