from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserForm
from users.models import User
from django.contrib.auth import authenticate, login


def forgot_view(request):
    return render(request, 'auth/forgot-password.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Invalid login credentials
            return render(request, 'auth/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'auth/login.html')


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login_view')
