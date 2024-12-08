from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'label', 'amount', 'category']  # Exclude the 'date' field


class OldExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'label', 'amount', 'category']  # Exclude the 'date' field


from django import forms
from django.contrib.auth.models import User


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Include the fields you want to update































from django import forms

class EMICalculatorForm(forms.Form):
    principal = forms.DecimalField(max_digits=10, decimal_places=2, label="Principal Amount")
    annual_interest_rate = forms.DecimalField(max_digits=5, decimal_places=2, label="Annual Interest Rate (%)")
    tenure = forms.IntegerField(label="Tenure (in years)")



from django import forms
from .models import Salary

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['amount']  # assuming 'amount' is the field for monthly salary
