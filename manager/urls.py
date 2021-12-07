
from django.urls import path,include
from manager import views

app_name = 'manager'

urlpatterns = [
    #Default and logged out views
    path("", views.index, name='index'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/signup/", views.signup_page, name="signup"),
    #Views that should require login
    path("home", views.home, name='home'),
    path("profile", views.profile, name='profile'),
    path("edit_profile", views.edit_profile, name='edit_profile'),
    path("create_profile", views.create_profile, name='create_profile'),
    path("create_party", views.create_party, name='create_party'),
    path("create_corporation", views.create_corporation, name='create_corporation'),
    path("create_union", views.create_union, name='create_union'),
    path("create_paramilitary", views.create_paramilitary, name='create_paramilitary'),
    path("create_assignment", views.create_assignment, name='create_assignment'),
]