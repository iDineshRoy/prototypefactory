from django import forms
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.contrib.auth import password_validation


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Email"}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"First Name"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Re-enter Password"}))

    def clean_password2(self, *args, **kwargs):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1!=p2:
            raise forms.ValidationError("Password didn't match. Please enter again.")
        else:
            return p1
    
    def clean_password1(self, *args, **kwargs):
        p = self.cleaned_data.get('password1')
        if len(smart_str(p, encoding='utf-8', strings_only=False, errors='strict'))<8:
            raise forms.ValidationError("Password must be at least 8 characters. Please enter again.")
        else:
            return p

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control mb-4", 'placeholder':"Password"}), label="")
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username':"",
            'password':""
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':"form-control mb-4", 'placeholder':'Username'})
        self.fields['username'].help_text = ""