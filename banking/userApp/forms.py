from socket import fromshare
from django import forms
from django.forms import ModelForm

from homeApp.models import Branches, District
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name',  'age', 'gender', 'phone', 'email', 'address', 'branch', 'account', 'cc', 'db', 'cb')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branches.objects.none()
