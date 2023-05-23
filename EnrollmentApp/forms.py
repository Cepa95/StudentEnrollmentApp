from django import forms
from .models import Predmeti, Korisnici

class PredmetForm(forms.ModelForm):
    nositelj = forms.ModelChoiceField(
        queryset=Korisnici.objects.filter(role='profesor'),
        empty_label='---------',
        label='Nositelj'
    )
    izborni = forms.ChoiceField(choices=Predmeti.IZBORNI, label='Izborni')

    class Meta:
        model = Predmeti
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.initial['izborni'] = instance.izborni


class KorisniciForm(forms.ModelForm):
    class Meta:
        model = Korisnici
        fields = '__all__'