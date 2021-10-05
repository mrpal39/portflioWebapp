
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.db.models import fields
from password_reset.forms import PasswordRecoveryForm, PasswordResetForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Profile
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()      
        self.fields['bio'].widget.attrs.update({"class":"form-control"})
        self.fields['image'].widget.attrs.update({"class":"image"})
        self.fields['email'].widget.attrs.update({"class":"form-control"})
        self.fields['phone'].widget.attrs.update({"class":"form-control"})
        self.fields['occupation'].widget.attrs.update({"class":"form-control"})

        self.fields['social_account'].widget.attrs.update({"class":"form-control"})
        self.fields['experence'].widget.attrs.update({"class":"form-control"})
        self.fields['skills'].widget.attrs.update({"class":"form-control"})
        self.fields['age'].widget.attrs.update({"class":"form-control"})
        self.fields['status'].widget.attrs.update({"class":"form-control"})
        self.fields['mobile'].widget.attrs.update({"class":"form-control"})
        self.fields['gender'].widget.attrs.update({"class":"form-control"})
        
    


class ProfilUpdateForm(UserForm):

    class Meta:

        model = Profile
        fields = (
         'bio',
         'image',
         'email',
         'phone',
         'social_account',
         'experence',
         'skills',
         'occupation',
         'age',
         'status',
         'mobile',
         'gender',

        )

    def __init__(self, *args, **kwargs):
        super(ProfilUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
       
        self.helper.add_input(Submit("submit", _("Save Changes")))

    def save(self):
        user = super().save(commit=False)
        user.save()
        return user


class ProfileForm(UserForm):

    class Meta:
        model = Profile
        fields = (
            'bio',
            'experence',
            'skills',
            'age',
            'status',
            'mobile',
            'gender',

        )
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit("submit", _("Save Changes")))

    def save(self):
        user = super().save(commit=False)
        user.save()
        return user
