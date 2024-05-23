from django import forms
from app.models import *
from django.core import validators
class CredForm(forms.Form):
    name=forms.CharField(max_length=250, required=False)
    pno =forms.CharField(max_length=250, required=False, validators=[validators.RegexValidator(r"\+91 ?[6-9]\d{9}")])
    email=forms.CharField(max_length=250, required=False, validators=[validators.RegexValidator(r"[A-Za-z]+\.?\w*\@[a-zA-Z]+\.[a-zA-Z]{2,3}")])
    username=forms.CharField(max_length=250, required=False)
    password=forms.CharField(max_length=250, required=False)
    profile=forms.ImageField(required=False)
    # class Meta:
    #     model = Credential
    #     fields = '__all__'
    #     validators = {'pno':[validators.RegexValidator(r"\+91 ?[6-9]\d{9}")],'email':[validators.RegexValidator(r"[A-Za-z]+\.?\w*\@[a-zA-Z]+\.[a-zA-Z]{2,3}")]}
    