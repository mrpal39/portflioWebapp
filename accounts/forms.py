from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.db import models
from password_reset.forms import PasswordRecoveryForm, PasswordResetForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from company.models import Company
from .models import  User 
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from  jobseeker.models import Profile

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": "autofocus"})
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True


class JobseekrForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"), widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(JobseekrForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class":"form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

        self.fields["username"].help_text = _(
            "Required. 30 characters or less. " "Only letters, numbers e @/./+/-/_."
        )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(JobseekrForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user = True

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.Jobseeker = True
        user.save()
        jobseeker = Profile.objects.create(user=user,bio="bio")
        return user


class CompanySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )
        
           
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.Company = True
        user.save()
        Companys = Company.objects.create(user=user,)
        return user




class UpdateUserForm(forms.ModelForm):
    class Meta:
        model =User    
        fields = (
                "first_name",
                "last_name",
                "email",
                "username",
                "roles",
            
            )                
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit("submit", _("Save Changes")))

    def save(self):
        user = super().save(commit=False)
        # user.request.user = True
        user.save()
        return user





class UsersPasswordRecoveryForm(PasswordRecoveryForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordRecoveryForm, self).__init__(*args, **kwargs)
        self.fields["username_or_email"].label = ""
        self.helper = FormHelper()
        self.helper.add_input(Submit("recover", _("Recover password")))


class UsersPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("recover", _("Recover password")))
