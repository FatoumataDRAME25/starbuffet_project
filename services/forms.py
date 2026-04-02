from django import forms
from. models import Traiteur

class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = ["fullname","speciality", "description", "adress", "email", "phone"]
