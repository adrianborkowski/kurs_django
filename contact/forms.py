from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

# Przykładowa metoda sprawdzająca
    def clean_name(self):
        data = self.cleaned_data['name']
        if "A" not in data:
            raise forms.ValidationError("Musisz mieć imię zaczynające się na 'A'!")
        return data