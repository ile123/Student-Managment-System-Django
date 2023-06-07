from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .models import Korisnik, Predmet
from django import forms

class User_Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
        
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'password', 'status', 'uloga']
    
    def clean_password(self):
        password = make_password(self.cleaned_data.get('password'))
        return password

class Subject_Form(forms.ModelForm):

    class Meta:
        model = Predmet
        fields = ['name', 'kod', 'program', 'ects', 'sem_izv', 'sem_red', 'izborni', 'nositelj']