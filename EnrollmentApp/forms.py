from django import forms
from .models import Predmeti, Korisnici

class PredmetiForm(forms.ModelForm):
    
    class Meta:
        model = Predmeti
        fields = '__all__'
