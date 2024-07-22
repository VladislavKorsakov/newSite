from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from .forms import TrustabilityForm
from .models import Trustability

def home_page(request):
    return render(request, 'main/index.html')


def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':'', 'email':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'main/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'main/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('home')


def profile_page(request):
    mail = get_user_model().objects.get(email=request.user.email)
    x1_education_db = Trustability.objects.get(email_connect=mail).education
    x1_age_db = Trustability.objects.get(email_connect=mail).age
    x1_kids_db = Trustability.objects.get(email_connect=mail).kids
    
    x1_education = None
    if x1_education_db == '0':
        x1_education = 10
    elif x1_education_db == '1':
        x1_education = 20
    elif x1_education_db == '2':
        x1_education = 40
    print(x1_education)
    
    x1_age = None
    if 18 <= x1_age_db <= 29:
        x1_age = 20
    elif x1_age_db <= 48:
        x1_age = 30
    elif x1_age_db >= 49:
        x1_age = 10
    print(x1_age)
    
    x1_kids = None
    if x1_kids_db == 0:
        x1_kids = 30
    elif 1 <= x1_kids_db <= 3:
        x1_kids = 20
    elif x1_kids_db > 3:
        x1_kids = 10
    print(x1_kids)
    
    x1_sum = (x1_education + x1_age + x1_kids)
    print(x1_sum)
    print('\t')
    
    
    x2_savings_db = Trustability.objects.get(email_connect=mail).savings
    x2_income_db = Trustability.objects.get(email_connect=mail).income
    x2_credit_db = Trustability.objects.get(email_connect=mail).credit
    x2_expenses_db = Trustability.objects.get(email_connect=mail).expenses
    
    x2_savings = None
    if x2_savings_db <= x2_income_db:
        x2_savings = 0
    elif x2_savings_db >= x2_income_db*5:
        x2_savings = 20
    elif x2_savings_db >= x2_income_db*3:
        x2_savings = 10
    print(x2_savings)
    
    x2_income = None
    if  x2_income_db <= x2_expenses_db:
        x2_income = 0
    elif x2_income_db - x2_expenses_db >= x2_income_db/1.5:
        x2_income = 30
    elif x2_income_db - x2_expenses_db >= x2_income_db/2:
        x2_income = 10
    print(x2_income)
    
    x2_credit = None
    if (x2_credit_db + x2_expenses_db) >= x2_savings_db:
        x2_credit = 0
    elif (x2_credit_db + x2_expenses_db) <= x2_savings_db/2:
        x2_credit = 20
    elif (x2_credit_db + x2_expenses_db) <= x2_savings_db/3:
        x2_credit = 10
    elif (x2_credit_db + x2_expenses_db) <= x2_savings_db:
        x2_credit = 10
    print(x2_credit)
    
    x2_expenses = None
    if x2_expenses_db >= x2_income_db:
        x2_expenses = 0
    elif x2_expenses_db <= x2_income_db/2:
        x2_expenses = 10
    elif x2_expenses_db <= x2_income_db/1.1:
        x2_expenses = 30
    else:
        x2_expenses = 0
    print(x2_expenses)
        
    x2_sum = (x2_savings + x2_income + x2_credit + x2_expenses)
    print(x2_sum)
    print('\t')
    
    
    x3_flat_db = Trustability.objects.get(email_connect=mail).flat
    x3_cars_db = Trustability.objects.get(email_connect=mail).cars
    x3_company_shares_db = Trustability.objects.get(email_connect=mail).company_shares
    
    x3_flat = None
    if x3_flat_db <= 0:
        x3_flat = 0
    elif x3_flat_db <= 2_000_000:
        x3_flat = 10
    elif x3_flat_db <= 4_000_000:
        x3_flat = 20
    elif x3_flat_db <= 6_000_000:
        x3_flat = 30
    elif x3_flat_db > 6_000_000:
        x3_flat = 40
    print(x3_flat)
        
    x3_cars = None
    if x3_cars_db <= 0:
        x3_cars = 0
    elif x3_cars_db <= 2_000_000:
        x3_cars = 10
    elif x3_cars_db <= 4_000_000:
        x3_cars = 20
    elif x3_cars_db <= 6_000_000:
        x3_cars = 30
    elif x3_cars_db > 6_000_000:
        x3_cars = 40
    print(x3_cars)
        
    x3_company_shares = None
    if x3_company_shares_db <= 0:
        x3_company_shares = 0
    elif x3_company_shares_db <= 3_000_000:
        x3_company_shares = 10
    elif x3_company_shares_db > 3_000_000:
        x3_company_shares = 20
    print(x3_company_shares)
    
    x3_sum = (x3_flat + x3_cars + x3_company_shares)
    print(x3_sum)
    print('\t')
    
    
    x4_social_activity_db = Trustability.objects.get(email_connect=mail).social_activity
    x4_opinion_db = Trustability.objects.get(email_connect=mail).opinion
    x4_colleagues_opinion_db = Trustability.objects.get(email_connect=mail).colleagues_opinion
    x4_work_db = Trustability.objects.get(email_connect=mail).work
    
    x4_social_activity = None
    if x4_social_activity_db <= 0:
        x4_social_activity = 0
    elif x4_social_activity_db <= 5:
        x4_social_activity = 10
    elif x4_social_activity_db >= 6:
        x4_social_activity = 20
    print(x4_social_activity)
        
    x4_opinion = None
    if x4_opinion_db <= 0:
        x4_opinion = 0
    elif x4_opinion_db <= 5:
        x4_opinion = 10
    elif x4_opinion_db >= 6:
        x4_opinion = 20
    print(x4_opinion)
        
    x4_colleagues_opinion = None
    if x4_colleagues_opinion_db <= 0:
        x4_colleagues_opinion = 0
    elif x4_colleagues_opinion_db <= 5:
        x4_colleagues_opinion = 10
    elif x4_colleagues_opinion_db >= 6:
        x4_colleagues_opinion = 20
    print(x4_colleagues_opinion)
        
    x4_work = None
    if x4_work_db <= 0:
        x4_work = 0
    elif x4_work_db <= 3:
        x4_work = 10
    elif x4_work_db <= 5:
        x4_work = 20
    elif x4_work_db <= 8:
        x4_work = 30
    elif x4_work_db >= 9:
        x4_work = 40
    print(x4_work)
    
    x4_sum = (x4_social_activity + x4_opinion + x4_colleagues_opinion + x4_work)
    print(x4_sum)
    print('\t')
    
    
    z = (0.15*x1_sum + 0.3*x2_sum + 0.25*x3_sum + 0.3*x4_sum)
    print(z)
    
    data = {
        'z': z
    }
    
    return render(request, 'main/profile.html', data)


def calculation_page(request):
    error = ''
    if request.method == 'POST':
        form = TrustabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error = 'Форма заполнена неправильно'
            
    form = TrustabilityForm()
    
    
    data = {
        'form': form,
        'error': error,
    }
        
    return render(request, 'main/calculation.html', data)