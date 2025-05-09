from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PredictionForm(forms.Form):
    Education = forms.ChoiceField(choices=[('Bachelors','Bachelors'), ('Masters','Masters'), ('PHD','PHD')])
    City = forms.ChoiceField(choices=[('Bangalore','Bangalore'), ('Pune','Pune'), ('New Delhi','New Delhi')])
    Gender = forms.ChoiceField(choices=[('Male','Male'), ('Female','Female')])
    EverBenched = forms.ChoiceField(choices=[('Yes','Yes'), ('No','No')])
    TenureGroup = forms.ChoiceField(choices=[('1-2','1-2'), ('>2','>2')])
    PaymentTier = forms.IntegerField()
    Age = forms.IntegerField()
    ExperienceInCurrentDomain = forms.FloatField()
    YearsInCompany = forms.FloatField()