from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if username is not None and len(username) < 3:
            self.add_error("username", "Username must be at least 3 characters long")

        if password1 is not None and len(password1) < 8:
            self.add_error("password1", "Password must be at least 8 characters long")

        if password1 is not None and password2 is not None and password1 != password2:
            self.add_error("password2", "Passwords do not match")
        
        return cleaned_data
