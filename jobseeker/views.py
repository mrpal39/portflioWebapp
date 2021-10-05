from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.forms import forms
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView

from .forms import ProfilUpdateForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from .models import Profile


def Profile_deshboard(request):

    user=Profile.objects.all()
        
    context={
        'objects':user
    }
    return render(request,'jobseeker/profile_jobseeker.html',context)


class Profile_create(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'jobseeker/profile_create.html'
    form_class = ProfileForm
    success_url = ('/')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        # jobseeker = Job.objects.create(user=user)
        # jobseeker.save()
        return user


class Profile_Update(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'jobseeker/profile_update.html'
    form_class = ProfilUpdateForm
    success_url = ('/')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        # jobseeker = Job.objects.create(user=user)
        # jobseeker.save()
        return user


class profile_detail(DetailView):
    model = Profile
    template_name='jobseeker/profile.html'
    context_object_name='objects'

