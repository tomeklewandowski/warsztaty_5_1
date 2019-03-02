from django import forms
from django.core.validators import EmailValidator


class LoginForm (forms.Form):
    username = forms.CharField(label="Login", strip=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserDataForm(forms.Form):
    first_name = forms.CharField(label="Imie", max_length=100)
    last_name = forms.CharField(label="Nazwisko", max_length=100)
    email = forms.CharField(label="mail", max_length=100, validators=[EmailValidator()])


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50, strip=True, label="Podaj login", help_text="Wpisz swój login")
    password = forms.CharField(label="Wpisz hasło", widget=forms.PasswordInput)
    password_again = forms.CharField(label="Wpisz hasło ponownie", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, strip=True, label="Dodaj imię", help_text="Wpisz imię z dużej litery")
    last_name = forms.CharField(max_length=50, strip=True, label="Dodaj nazwisko", help_text="Wpisz nazwisko z dużej litery")
    email = forms.EmailField(max_length=50, label="Podaj swój email")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")

        if password != password_again:
            raise forms.ValidationError(
                "password and password_again does not match")

