from django.urls import path

from . import views



urlpatterns = [
    path('',views.Profile_deshboard, name='profile_job'),
    # path('Create/',views.Profile_create.as_view(), name='profile_Create'),
    path('Update/<pk>/',views.Profile_Update.as_view(), name='profile_Update'),
    path('f/<pk>',views.profile_detail.as_view(), name='profile_Detail'),
]
