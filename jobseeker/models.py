from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, EmailField
from django.urls import reverse
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect

from accounts.models import User

# Create your models here.


class Occupation(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)

    def __str__(self):
        return self.name


class social_conect(models.Model):
    platform_name = models.CharField(max_length=100, default='facebook')
    platform_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.platform_name} Profile {self.pk} '


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True, default='3')
    image = models.ImageField(upload_to="media/",default='assets/img/avataaars.svg')
    email = EmailField(default='admin@gmial.com')
    phone = models.IntegerField(default='012345678')
    social_account = models.ManyToManyField(social_conect)
    experence = models.CharField(max_length=100, default='d')
    occupation=models.CharField(max_length=100)
    skills = models.CharField(max_length=100, default='d')
    age = models.CharField(max_length=100, default='d')
    status = models.CharField(max_length=100, default='d')
    mobile = models.CharField(max_length=100, default='d')
    gender = models.CharField(max_length=100, default='d')

    def __str__(self):
        return f'{self.user} Profile {self.pk} '

    def save(self, *args, **kwargs):

        # Call the real save() method
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return HttpResponseRedirect('/')


class Review(models.Model):

    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    profile_rating = models.ForeignKey(
        Profile, null=True, on_delete=models.CASCADE)
    review_created = models.DateTimeField('Date of Review', auto_now_add=True)
    reviewer_name = models.CharField(max_length=55, default='admin')
    reviewer_city = models.CharField(max_length=55, default='kaithal')
    reviewer_state = models.CharField(max_length=2, default='hr')
    email = models.EmailField(default='admin@gmail.com')
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    review_comment = models.TextField(default='Great Work')
    review_slug = models.SlugField(default='')

    def get_absolute_url(self):
        # return reverse('lawyer_createreview', kwargs={'review_slug': self.review_slug})
        return reverse('homepage')

    def __str__(self):
        return f'{self.review_slug}or{self.profile_rating}'

    def save(self, *args, **kwargs):

        # Call the real save() method
        super(Review, self).save(*args, **kwargs)



