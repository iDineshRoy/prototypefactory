from dataclasses import fields
from django import forms

from .models import Project

class ProjectModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Title"}))
    # location = forms.ChoiceField()
    company = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Company"}))
    resources = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Resources"}))
    
    class Meta:
        model = Project
        fields = ["title", "description", "location","industry","company", "resources"]