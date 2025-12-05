from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.formfields import PhoneNumberField
from Cart.models import Cart

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Account Name',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder' : 'Account Password',
    'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder' : 'Account Email',
    'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder' : 'Account Phone Number',
    'class' : 'w-full py-4 px-6 rounded-xl',
    }))

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')

        user = User.objects.filter(username=username).first()
        if not user:
            return cleaned_data
        
        cart, created = Cart.objects.get_or_create(user=user)

        try:
            submitted = PhoneNumber.from_string(phone_number, region='US')
        except:
            raise forms.ValidationError("Invalid phone number format.")
        
        if cart.phoneNumber != submitted: 
            raise forms.ValidationError("Incorrect phone number please try again.")
        
        if cart.user.email != email:
            raise forms.ValidationError("Incorrect email please try again")
        
        return cleaned_data
    

class SignupForm(UserCreationForm):
    # this adds a extra input field for users signing in
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    phone_number = PhoneNumberField(region="US", widget=forms.TextInput(attrs={
        'placeholder' : 'Phone Number',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    class Meta:
        model = User
        fields = ('username','password1','password2','email')


    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Name',
    'class': 'w-full py-4 px-6 rounded-xl',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': 'w-full py-4 px-6 rounded-xl',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password',
    'class': 'w-full py-4 px-6 rounded-xl',
    }))

    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']
        user.save()

        phone = self.cleaned_data['phone_number']

        cart, created = Cart.objects.get_or_create(user=user)
        cart.phoneNumber = phone
        cart.save()
        
        return user