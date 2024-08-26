from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput,TextInput



#-- registration from (create a user)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # for field in ['username', 'password1', 'password2'] :
        #     self.fields[field].widget.attrs.update({
        #         'class': 'form-control',
        #         'placeholder':  f'Enter {field}'
        #     })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Re-enter password'
        })


#-- login form ( login a user )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput(attrs={"class":"form-control" , "placeholder" : "Username"}))
    password = forms.CharField(widget = PasswordInput(attrs={"class":"form-control" , "placeholder" : " Password"}))
