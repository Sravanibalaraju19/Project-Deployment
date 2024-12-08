from django.shortcuts import render
from .models import Expense


def employee_homepage(request):
    return render(request, 'employeeapp/employee_homepage.html')


from django.shortcuts import render, redirect


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('expense_success')  # Redirect to a success page
    else:
        form = ExpenseForm()

    return render(request, 'employeeapp/add_expense.html', {'form': form})


from django.contrib.auth.decorators import login_required

sample_expense_data = {
    'categories': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transport'],
    'amounts': [1200, 400, 200, 150, 100],
}


@login_required
def employee_dashboard(request):
    # Fetch the actual employee's expense data from the database here
    # For now, we're using the sample data
    return render(request, 'employeeapp/dashboard.html', {'expense_data': sample_expense_data})


from django.contrib.auth.decorators import login_required


@login_required
def employee_dashboard(request):
    # Your dashboard logic
    return render(request, 'employeeapp/dashboard.html')


from django.shortcuts import redirect

from django.contrib.auth import logout as auth_logout
from django.urls import reverse


def logout_view(request):
    auth_logout(request)
    return redirect(reverse('login'))



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the expense with valid data
            return redirect('view_expenses')  # Redirects to another page
    else:
        form = ExpenseForm()
    return render(request, 'employeeapp/add_expense.html', {'form': form})


@login_required
def view_expenses(request):
    # Fetch the logged-in user's expenses, ordered by label or any other field
    expenses = Expense.objects.filter(user=request.user).order_by('label')
    return render(request, 'employeeapp/view_expenses.html', {'expenses': expenses})


from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Form for EMI Calculator
class EMICalculatorForm(forms.Form):
    principal = forms.DecimalField(label="Principal Amount", min_value=0, decimal_places=2)
    rate_of_interest = forms.DecimalField(label="Rate of Interest (per annum in %)", min_value=0, decimal_places=2)
    tenure = forms.IntegerField(label="Loan Tenure (in months)", min_value=1)


def emi_calculator(request):
    emi_amount = None
    if request.method == "POST":
        try:
            # Get loan amount, interest rate, and loan term from form input
            loan_amount = Decimal(request.POST.get('loan_amount'))
            interest_rate = Decimal(request.POST.get('interest_rate'))
            loan_term = int(request.POST.get('loan_term'))

            # EMI calculation logic
            monthly_interest_rate = interest_rate / 12 / 100
            number_of_months = loan_term * 12

            emi_amount = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months
            emi_amount /= (1 + monthly_interest_rate) ** number_of_months - 1

        except Exception as e:
            # If there is an error, we can return a message or log it
            print(f"Error calculating EMI: {e}")
            return HttpResponse("Error calculating EMI", status=500)

    # Render the template and pass the EMI amount to the context
    return render(request, 'employeeapp/emi_calculator.html', {'emi_amount': emi_amount})



from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

# View function for Tax Calculator
def tax_calculator(request):
    calculated_tax = None
    if request.method == "POST":
        try:
            # Get income and tax rate from form input
            income = Decimal(request.POST.get('income'))
            tax_rate = Decimal(request.POST.get('tax_rate'))

            # Calculate the tax
            calculated_tax = (income * tax_rate) / 100  # simple tax calculation
        except Exception as e:
            # If there is an error, we can return a message or log it
            print(f"Error calculating tax: {e}")
            return HttpResponse("Error calculating tax", status=500)

    # Render the template and pass the calculated tax to the context
    return render(request, 'employeeapp/tax_calculator.html', {'calculated_tax': calculated_tax})



from django.shortcuts import render
import requests

# View function for Currency Converter
def currency_converter(request):
    currencies = ['USD', 'EUR', 'INR']
    converted_amount = None

    if request.method == "POST":
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))

        # Example static conversion rates (replace with actual API data or calculations)
        conversion_rates = {
            'USD': {'EUR': 0.94, 'INR': 75.15, 'GBP': 0.82},
            'EUR': {'USD': 1.06, 'INR': 80.10, 'GBP': 0.87},
            'INR': {'USD': 0.013, 'EUR': 0.012, 'GBP': 0.011},
            # Add more conversion rates here as required
        }

        # Convert the amount if valid currencies are provided
        if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
            rate = conversion_rates[from_currency][to_currency]
            converted_amount = amount * rate

    return render(request, 'employeeapp/currency_converter.html', {'currencies': currencies, 'converted_amount': converted_amount})


from django.shortcuts import render
from .forms import SalaryForm

from django.shortcuts import render, redirect
from .models import Employee

def add_salary(request):
    if request.method == "POST":
        salary = request.POST.get('salary')
        employee = Employee.objects.create(salary=salary)
        return redirect('budget_overview', employee_id=employee.id)
    return render(request, 'employeeapp/add_salary.html')

from decimal import Decimal

# views.py
from django.shortcuts import render
from .models import Employee
from .models import Salary
from decimal import Decimal

def budget_overview(request, employee_id):
    # Fetch salary details using employee_id
    salary = Employee.objects.get(id=employee_id).salary  # Example fetch

    # Ensure salary is in Decimal for accurate calculation
    salary = Decimal(salary)

    # Example budget allocation (you can adjust these percentages as needed)
    housing_expense = Decimal(0.30)  # 30% for housing
    food_expense = Decimal(0.20)  # 20% for food
    transportation_expense = Decimal(0.15)  # 15% for transportation

    # Perform calculations
    housing = salary * housing_expense
    food = salary * food_expense
    transportation = salary * transportation_expense

    # Pass calculated values to the template
    context = {
        'salary': salary,
        'housing': housing,
        'food': food,
        'transportation': transportation
    }
    return render(request, 'employeeapp/budget_overview.html', context)
