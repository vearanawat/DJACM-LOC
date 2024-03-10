from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['age', 'education_qualification', 'years_of_experience', 'current_salary', 'gender']
