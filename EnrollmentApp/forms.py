from django import forms
from .models import Predmeti, Korisnici


class PredmetForm(forms.ModelForm):
    nositelj = forms.ModelChoiceField(
        queryset=Korisnici.objects.filter(role='profesor'),
        empty_label='---------',
        label='Nositelj'
    )

    class Meta:
        model = Predmeti
        fields = '__all__'
