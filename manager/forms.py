from django import forms
from django.forms import widgets
from manager.models import *

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'character_name',
            'region',
            'corporation',
            'paramilitary',
            'union',
            'party',
        ]


#Add more fields!
class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ['name']

class ParamilitaryForm(forms.ModelForm):
    class Meta:
        model = Paramilitary
        fields = ['name','country','type']

class CorporationForm(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = ['name','specialization']

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['name','country']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name','content']