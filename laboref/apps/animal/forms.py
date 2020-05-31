from django import forms

from .models import Animal


class EditAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_name', "animal_age", "animal_breed", "animal_color")


class NewAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('' 'animal_name', "animal_age", "animal_breed", "animal_color")
