from django.shortcuts import render

from django.shortcuts import render

def user_homepage(request):
    return render(request, 'userapp/user_homepage.html')

