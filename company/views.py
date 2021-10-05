from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.

from django.views.generic.edit import BaseCreateView, CreateView, UpdateView
from company.forms import Job_Create_From
from django.db import transaction

from company.models import Company, Job


class companyProfileView(TemplateView):
    model=Company
    template_name='companyProfile.html'




class Job_Create(LoginRequiredMixin, CreateView):
    model = Job
    template_name ='create.html'
    form_class=Job_Create_From
    success_url=('/')    

    def form_valid(self, form):
        form.instance.hr_name = self.request.user
        return super().form_valid(form)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        # jobseeker = Job.objects.create(user=user)
        # jobseeker.save()
        return user


class job_update(UpdateView):
    model = Job
    template_name ='job_update.html'
    form_class=Job_Create_From
    success_url=('')  

    def form_valid(self, form):
        form.instance.hr_name= self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.hr_name:
            return True
        return False



class employeDetail(DetailView):

    model = Job
    template_name='jobdetail.html'  
    context_object_name='objects' 


    def get_context_data(self, **kwargs):
        context = super(employeDetail, self).get_context_data(**kwargs)
        context['user']=Employe.objects.all()
        return context     