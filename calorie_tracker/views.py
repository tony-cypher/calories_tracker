from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Food, Consume
from .forms import LoginForm, RegisterForm

# Create your views here. 

# this login was created to custoomize the login form.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'calorie_tracker/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Welcome {username}, your account is created !')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'calorie_tracker/register.html', {'form':form})

@login_required
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        
    consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    context = {
        'foods':foods, 
        'consumed_food':consumed_food
    }
    return render(request, 'calorie_tracker/index.html', context)

@login_required
def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete();
        return redirect('/')
    else:
        return render(request, 'calorie_tracker/delete.html')