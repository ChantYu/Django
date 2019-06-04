from django import forms
from LoginApp.models import UserProfileInfo, Gender ,Company
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
#class GenderForm(forms.ModelForm):
#     class Meta():
#         model = Gender
#         fields = ('gender')
#class CompanyForm(forms.ModelForm):
#     class Meta():
#         model = Company
#         fields = ('company_name')		 