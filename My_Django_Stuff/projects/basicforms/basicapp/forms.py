from django import forms
from django.core import validators


# custom validator
def check_for_z(value: str):
    if value[0] != 'Z':
        raise forms.ValidationError("Name must start with Z")


class Form(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email doesn't match!")
