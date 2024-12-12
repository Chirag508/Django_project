from django import forms
from .models import customer_data

class customer_form(forms.ModelForm):
    class Meta:
        model = customer_data
        fields = ['name','phone','age','address','state']