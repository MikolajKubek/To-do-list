from django import forms

class TodoForm(forms.Form):
    content = forms.CharField(
         widget = forms.TextInput(
            attrs = {
                'placeholder': 'what?',
                'class': 'form-control',
            }
        )
    )
    date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'], widget = forms.DateTimeInput(
        attrs={
            'placeholder': 'when?',
            'class': 'form-control',
        }))

class LoginForm(forms.Form):
    username = forms.CharField(         
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        ))
    password = forms.CharField(         
        widget = forms.TextInput(
            attrs = {
                'type': 'password',
                'class': 'form-control',
            }
        ))