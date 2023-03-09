from django import forms
from .models import Cattle,Farmer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CattleForm(forms.ModelForm):
    
    class Meta:
        model = Cattle
        fields = ("__all__")

class FarmerForm(forms.ModelForm):
    
    class Meta:
        model = Farmer
        fields = ("__all__")
        
               


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']  