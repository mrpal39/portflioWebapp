import django
from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.enums import Choices
from django.forms.models import ModelFormMetaclass
from django.shortcuts import redirect
from django.urls.base import clear_url_caches
from accounts.models import User
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    company_sizes = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=10, blank=True, null=True)
    size = models.CharField(default=1, choices=company_sizes,max_length=1)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(default='')
    description = models.TextField(default='')
    slugs = models.SlugField(default='hbjhjh')
    
    
    def __str__(self):

        return self.user.first_name


class Job(models.Model):
    title = models.CharField(max_length=100, default="ok", blank=True)
    hr_name = models.ForeignKey(User, on_delete=models.CASCADE)

    postion = models.CharField(max_length=100, default="ok", blank=True)
    salary = models.CharField(max_length=100, default="ok", blank=True)
    requrements = models.CharField(max_length=100, default="ok", blank=True)
    job_tpe = models.CharField(max_length=100, default="ok", blank=True)
    job_time = models.CharField(max_length=100, default="ok", blank=True)
    job_info = models.CharField(max_length=100, default="ok", blank=True)
  
    def get_absolute_url(sefl):
        return redirect("/")

    def __str__(self):
        return self.title


class Review(models.Model):

    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    review_created = models.DateTimeField('Date of Review', auto_now_add=True)
    reviewer_name = models.CharField(max_length=55, default='')
    reviewer_city = models.CharField(max_length=55, default='')
    reviewer_state = models.CharField(max_length=2, default='')
    email = models.EmailField(default='')
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    review_comment = models.TextField(default='')
    review_slug = models.SlugField(default='')

    def get_absolute_url(self):
        # return reverse('lawyer_createreview', kwargs={'review_slug': self.review_slug})
        return reverse('homepage')

    def __str__(self):
        return self.review_slug



class CompanyJobs(models.Model):
    job_id=models.IntegerField(null=True,blank=True)
    title=models.CharField(max_length=254,null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    department=models.TextField(null=True,blank=True)
    salary_range=models.TextField(null=True,blank=True)
    company_profile=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    requirements=models.TextField(null=True,blank=True)
    benefits=models.TextField(null=True,blank=True)
    telecommuting=models.TextField(null=True,blank=True)
    has_company_logo=models.TextField(null=True,blank=True)
    has_questions=models.TextField(null=True,blank=True)
    employment_type=models.TextField(null=True,blank=True)
    required_experience=models.TextField(null=True,blank=True)
    required_education=models.TextField(null=True,blank=True)
    industry=models.TextField(null=True,blank=True)
    functions=models.TextField(null=True,blank=True)
    fraudulent=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
