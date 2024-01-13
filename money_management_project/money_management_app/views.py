from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Transaction

@login_required
def index(request):
    transactions = Transaction.objects.all()
    net_value = sum([t.amount if t.type == 'income' else -t.amount for t in transactions])
    return render(request, 'money_management_app/index.html', {'transactions': transactions, 'net_value': net_value, 'user': request.user})

@login_required
def income(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        category = request.POST['category']
        Transaction.objects.create(amount=amount, category=category, type='income')
        return redirect('index')
    return render(request, 'money_management_app/income.html')

@login_required
def expense(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        category = request.POST['category']
        Transaction.objects.create(amount=amount, category=category, type='expense')
        return redirect('index')
    return render(request, 'money_management_app/expense.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form, 'user': request.user})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                return redirect('index')  # Redirect to the home page after successful login
            else:
                # Authentication failed
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'user': request.user})

@login_required
def user_logout(request):
    logout(request)
    return redirect('register')
