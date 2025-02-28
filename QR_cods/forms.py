from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["card_number"]
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': 'Enter card number'})
        }