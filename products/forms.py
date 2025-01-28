from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Message',
        'class': 'form-control',
        'rows': 5
    }))
# from django import forms

# class JoinUsForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
#     )
#     message = forms.CharField(
#         required=False,
#         widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Why do you want to join?'}),
#     )

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']  # Add any other fields you want to include
