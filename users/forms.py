from django import forms
from django.contrib.auth import get_user_model  # Standart User o'rniga shu ishlatiladi
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Dinamik ravishda siz yaratgan 'users.UserModel'ni oladi
User = get_user_model()


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):  # UserCreationForm.Meta'dan voris olamiz
        model = User  # Endi bu sizning yangi modelingizga ishora qiladi
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]  # UserCreationForm'da password1/2 maydonlari ichkarida avtomat bo'ladi


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  # Bu yerda ham sizning yangi modelingiz ishlaydi
        fields = ['first_name', 'last_name', 'email']



