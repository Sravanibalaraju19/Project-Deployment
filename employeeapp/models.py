
from django.db import models

class OldExpense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.amount}"

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)  # Expense label (could be name)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Expense amount
    category = models.CharField(max_length=50)  # Expense category (if needed)
    date = models.DateField(auto_now_add=True)  # This ensures the date is auto-filled on creation

    def __str__(self):
        return f"{self.label} - {self.amount}"



from django.db import models

class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Salary: {self.amount}"


# models.py

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def calculate_budget(self):
        # Example budget categories
        necessities = self.salary * 0.50  # 50% of salary
        savings = self.salary * 0.20  # 20% of salary
        leisure = self.salary * 0.10  # 10% of salary
        others = self.salary * 0.20  # 20% of salary
        return necessities, savings, leisure, others
