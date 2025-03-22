from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'

from .models import University

class UniversityData(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'  # Include all fields from the University model
