from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Lesson
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import ModelForm, DateTimeInput


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class BookLessonForm(ModelForm):

    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'autocomplete': 'off'}))
    # date_time = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     }))
    class Meta:
        model=Lesson
        fields=('teacher', 'date_time')
