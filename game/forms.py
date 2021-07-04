from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

from . import models


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации """
    email = forms.EmailField(max_length=150)
    username = forms.CharField(max_length=150, label='Имя пользователя:')
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput, label='Пароль:')
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput, label='Подтвердите пароль:')
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email...'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password...'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Password confirmation...'}),
        }


class UserLoginForm(AuthenticationForm):
    """Форма для авторизации """
    username = forms.CharField(max_length=150, label='Имя пользователя:')
    password = forms.CharField(max_length=150, label='Пароль:', widget=forms.PasswordInput)


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = models.Reviews
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=models.RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = models.Rating
        fields = ('star', )
