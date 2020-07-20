from django import forms
from app.models import Admintable,Scheduletable
from django.forms import PasswordInput,DateInput,NumberInput,TimeInput

class Adminform(forms.ModelForm):
    class Meta:
        model=Admintable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}

class Scheduleform(forms.ModelForm):
    class Meta:
        model=Scheduletable
        fields="__all__"