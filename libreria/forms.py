from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Libro, Profile  # Asegúrate de importar Profile
import re

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 12:
            raise forms.ValidationError("La contraseña debe tener al menos 12 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("La contraseña debe tener al menos una letra minúscula.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("La contraseña debe tener al menos un número.")
        if not re.search(r'[\W]', password):
            raise forms.ValidationError("La contraseña debe tener al menos un carácter especial.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 16:
            raise forms.ValidationError("El nombre de usuario no puede tener más de 16 caracteres.")
        if re.match(r'^[0-9]', username):
            raise forms.ValidationError("El nombre de usuario no puede comenzar con un número.")
        return username

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagen']

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nuevo Usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Nuevo Correo Electrónico'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if not username and not email:
            raise forms.ValidationError("Debe llenar al menos uno de los campos.")
        
        return cleaned_data
