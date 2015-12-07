from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms  import ProfileForm, PortfolioForm
from .models import  Developer, Portfolio
# Create your views here.

# this directs you to the developers profile page i.e. /profile/me

@login_required(login_url='/')
def profile(request):
    return render(request,'profile.html')

# this line edits the current user by pre loading their details from github i.e names and email

@login_required(login_url='/')
def edit_profile(request):
     dev_profile = Developer.objects.get(id=request.user.pk)
     profile_form = ProfileForm(instance=dev_profile)
     return render(request,'register.html',context= {'profile_form' : profile_form})


@login_required(login_url='/')
def new_portfolio(request):
    portfolio_form = PortfolioForm
    return render(request,'register_portfolio.html',context= {'portfolio_form' : portfolio_form})

# this is where we create the user


@login_required(login_url='/')
def create_profile(request):
    if request.method == 'POST':
        dev_profile = Developer.objects.get(id=request.user._get_pk_val)
        profile_form = ProfileForm(request.POST or None,instance=dev_profile)
        if profile_form.is_valid():
           profile_form.save()
           return redirect('/profile/me/')
    return render(request,'register.html',context={'profile_form' : profile_form})


@login_required(login_url='/')
def create_portfolio(request):
     # dev = Developer.objects.get(pk=request.user._get_pk_val)
     if request.method == 'POST':
         portfolio_form = PortfolioForm(request.POST,request.FILES)
         if portfolio_form.is_valid():
             portfolio = portfolio_form.save(commit=False)
             portfolio.owner_id = request.user.id
             portfolio.save()
             portfolio_form.save_m2m()
             return redirect('/profile/me/')
     return render(request,'register_portfolio.html',context= {'portfolio_form' : portfolio_form})
