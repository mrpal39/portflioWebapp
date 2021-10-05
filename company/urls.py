from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [

    path('',views.companyProfileView.as_view(),name='companyProfileView'),

    path('job/',views.Job_Create.as_view(),name='job_create'),
    path('job/update/<pk>/',views.job_update.as_view(),name='job_update'),
    path('job/detail/<pk>/',views.employeDetail.as_view(),name='job_Detail')

]