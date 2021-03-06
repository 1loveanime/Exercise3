from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import IdolDetail

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class IdolCreationForm(forms.ModelForm):
	class Meta:
		model = IdolDetail
		exclude = ('', )