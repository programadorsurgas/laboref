from django import forms

from .models import Animal


class EditAnimalForm(forms.Form):
    class Meta:
        model = Animal
        fields = '__all__'
