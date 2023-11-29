from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from salama.models import salama_register, OrderForm


class register_form(forms.ModelForm):
    class Meta:
        model = salama_register
        fields = '__all__'
        widgets = {
            field.name: forms.TextInput(attrs={'placeholder': f'Your {field.verbose_name}'})
            for field in salama_register._meta.fields
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class Salama_OrderForm(forms.ModelForm):
     class Meta:
        model = OrderForm
        fields = ['item', 'description', 'quantity', 'route']
        # fields = '__all__'

        widgets = {
            field.name: forms.TextInput(attrs={'placeholder': f' {field.verbose_name}'})
            for field in OrderForm._meta.fields
        }
