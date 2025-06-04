from .models import Deal
from django import forms

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['client', 'manager', 'title', 'amount', 'status']