from django.urls import path 
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('UserHome/', views.UserHome, name='UserHome')
]