from django.http import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    data = {
            "page_title":"Index",
        }
    return render(request,"manager/index.html",data)


def signup_page(request):
    if request.method == "GET":
        data = {
            "form": UserCreationForm(),
            "page_title":"Signup",
        }
        return render(request, "registration/signup.html", context=data)

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return redirect("login")