from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = Account
#         fields = '__all__'


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='password2', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    class Meta:
        model = User
        fields = ('email','username', 'first_name', 'last_name')
                
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        # cleanPass = self.cleaned_data[self.clean_password2()]
        user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user
    


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
