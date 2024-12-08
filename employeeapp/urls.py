from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_homepage, name='employee_homepage'),  # employee homepage
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('view_expenses/', views.view_expenses, name='view_expenses'),
    path('emi_calculator/', views.emi_calculator, name='emi_calculator'),
    path('tax_calculator/', views.tax_calculator, name='tax_calculator'),
    path('currency_converter/', views.currency_converter, name='currency_converter'),
    path('add_salary/', views.add_salary, name='add_salary'),
    path('employees/budget_overview/<int:employee_id>/', views.budget_overview, name='budget_overview'),
]
