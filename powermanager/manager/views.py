from django.http import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from manager.models import *
from manager.forms import *
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    data = {
            "page_title":"Landing Page",
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
        return redirect("accounts:login")

#Logged in views

@login_required
def home(request):
    data = {
            "page_title":"Home",
        }
    return render(request,'manager/home.html',data)

@login_required
def profile(request):
    try:
        account = Account.objects.get(owner=request.user)
    except:
        return redirect("manager:create_profile")
    data = {
            "page_title":"Profile",
            "item": account,
        }
    return render(request,'manager/item.html',data)

@login_required
def edit_profile(request):
    return render(request,'manager/home.html')

@login_required
def create_profile(request):
    if request.method == "GET":
        data = {
            "name": "Profile",
            "form": AccountForm(),
            "page_title":"Create Account",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = AccountForm(request.POST)
        new_account = form.save(commit=False)
        new_account.owner = request.user
        new_account.save()
        return redirect("manager:home")

@login_required
def create_union(request):
    if request.method == "GET":
        data = {
            "name": "Union",
            "form": UnionForm(),
            "page_title":"Create Union",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = UnionForm(request.POST)
        form.save()
        return redirect("manager:profile")

@login_required
def create_party(request):
    if request.method == "GET":
        data = {
            "name": "Party",
            "form": PartyForm(),
            "page_title":"Create Union",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = PartyForm(request.POST)
        form.save()
        return redirect("manager:profile")

@login_required
def create_corporation(request):
    if request.method == "GET":
        data = {
            "name": "Corporation",
            "form": CorporationForm(),
            "page_title":"Create Corp",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = CorporationForm(request.POST)
        form.save()
        return redirect("manager:profile")

@login_required
def create_paramilitary(request):
    if request.method == "GET":
        data = {
            "name": "Paramilitary",
            "form": ParamilitaryForm(),
            "page_title":"Create Paramilitary",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = ParamilitaryForm(request.POST)
        form.save()
        return redirect("manager:profile")

@login_required
def create_assignment(request):
    if request.method == "GET":
        data = {
            "name": "Assignment",
            "form": AssignmentForm(),
            "page_title":"Create Assignment",
        }
        return render(request, "manager/create_item.html", context=data)

    elif request.method == "POST":
        form = AssignmentForm(request.POST)
        form.save()
        return redirect("manager:profile")



