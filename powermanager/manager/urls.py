
from django.urls import path,include


from manager import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
]