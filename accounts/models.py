from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import AutoField
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

def get_sentinel_user():

    return get_user_model().objects.get_or_create(username='deleted')[0]
# Create your models here.


class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  Jobseeker = 1
  Company = 2
  SECRETARY = 3
  SUPERVISOR = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (Jobseeker, 'jobseeker'),
      (Company, 'company'),
      (SECRETARY, 'secretary'),
      (SUPERVISOR, 'supervisor'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class User(AbstractUser):
    roles = models.ManyToManyField(Role)  
    def get_absolute_url(self):
        return reverse("user_profile", args=[self.id])
    def __str__(self):
        return self.first_name





class SECRETARY(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True)
   
    def __str__(self):
        return f'{self.user} Profile'

    
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk': self.pk})


class admin(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True)
   
    def __str__(self):
        return f'{self.user} Profile'

    
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk': self.pk})

class SUPERVISOR(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True)
   
    def __str__(self):
        return f'{self.user} Profile'

    
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk': self.pk})

