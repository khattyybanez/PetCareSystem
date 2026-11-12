from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'pet_type',
            'breed',
            'age',
            'gender',
            'color',
            'owner_name',
            'owner_contact',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pet name'
            }),
            'pet_type': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter breed'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age in years',
                'min': 0
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter color'
            }),
            'owner_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter owner's name"
            }),
            'owner_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter owner's contact number"
            }),
        }