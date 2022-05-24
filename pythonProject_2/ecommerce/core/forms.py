from django import forms
from core.models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        field = '__all__'
