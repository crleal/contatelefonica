from django import forms
from models import conta


class FormConta(forms.ModelForm):
    class Meta:
        model = conta
