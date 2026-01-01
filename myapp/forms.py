from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        }),
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'form-control'
        }),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username',
                'class': 'form-control'
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists. Please choose another.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError({
                    'confirm_password': 'Passwords do not match.'
                })

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'form-control'
        })
    )


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Enter your complete shipping address',
            'class': 'form-control'
        }),
        label='Shipping Address'
    )
    contact_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Enter your contact number',
            'class': 'form-control',
            'pattern': '[0-9]{10,15}'
        }),
        label='Contact Number'
    )

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        # Remove any non-digit characters
        contact_number = ''.join(filter(str.isdigit, contact_number))
        
        if len(contact_number) < 10 or len(contact_number) > 15:
            raise ValidationError('Contact number must be between 10 and 15 digits.')
        
        return contact_number

    def clean_shipping_address(self):
        shipping_address = self.cleaned_data.get('shipping_address').strip()
        if len(shipping_address) < 10:
            raise ValidationError('Please provide a complete shipping address (minimum 10 characters).')
        return shipping_address


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search any product...',
            'class': 'form-control'
        }),
        label='Search Products'
    )

