from django.urls import path

app_name = 'core'
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('jobs/', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('applications/', views.application_list, name='application_list'),

]



