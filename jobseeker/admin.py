from django.contrib import admin

from .models import Occupation, Profile, Review,  social_conect

admin.site.register(Profile)

admin.site.register(Review)
admin.site.register(social_conect)
admin.site.register(Occupation)
