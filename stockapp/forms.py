from django import forms
from django.forms import ModelForm


class StockForm(forms.Form):
    stockname = forms.CharField(max_length=12)