from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, ChildInfo, Education

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info' ]
        widgets = {
            'image': forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Add information'})
        }

class ChildInfoForm(ModelForm):
    class Meta:
        model = ChildInfo
        fields = ['name', 'gender', 'date_of_birth', 'medical_condition']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Add child's name"}),
            'gender': forms.TextInput(attrs={'placeholder': 'select between male and female'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder':'add the start school date'}),
            'medical_condition': forms.Textarea(attrs={'rows': 4,'placeholder': 'comma separated values if more than one'})
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'location', 'from_date', 'to_date']
        widgets = {
            'school': forms.TextInput(attrs={'placeholder': 'Add current school'}),
            'location': forms.TextInput(attrs={'placeholder': 'Add the school location'}),
            'from_date': forms.DateInput(attrs={'placeholder':'add the start school date'}),
            'to_date': forms.DateInput(attrs={'placeholder': 'Add the date to finish school'})
        }

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']
