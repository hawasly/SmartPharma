from asyncore import compact_traceback
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name' , 'note']