
from django.urls import path,include
from manager import views

app_name = 'manager'

urlpatterns = [
    path("", views.index, name='index'),

    path("auth/", include('django.contrib.auth.urls')),
    
    # Sign up a new user
    path("auth/signup/", views.signup_page, name="signup")
]