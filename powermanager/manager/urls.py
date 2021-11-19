
from django.urls import path,include
from manager import views

app_name = 'manager'

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home_page, name='home'),
    path("view/", views.view_page, name='view'),
    path("edit/", views.edit_page, name='edit'),
    
    path("auth/", include('django.contrib.auth.urls')),
    
    # Sign up a new user
    path("auth/signup/", views.signup_page, name="signup")
]