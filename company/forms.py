from django import forms

from .models import Job

from django.db import transaction

class Job_Create_From(forms.ModelForm):
    class Meta:

        model = Job
        fields = (
            'title',
            'postion',
            'salary',
            'requrements',
            'job_tpe',
            'job_time',
            'job_info',

        )

