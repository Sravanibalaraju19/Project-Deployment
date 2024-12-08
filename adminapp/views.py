from django.shortcuts import render, redirect

from django.shortcuts import render


def homepage(request):
    return render(request, 'adminapp/homepage.html')


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        print(username)

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/homepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect based on username length
            if len(username) == 4:
                return redirect('employee_homepage')
            elif len(username) == 10:
                return redirect('user_homepage')
            else:
                return redirect('homepage')
    return render(request, 'adminapp/login.html')


from django.shortcuts import render

def about_us(request):
    return render(request, 'adminapp/about_us.html')

def contact(request):
    return render(request, 'adminapp/contact.html')