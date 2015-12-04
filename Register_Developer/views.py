from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms  import DeveloperRegistrationForm
from .models import  Developer
# Create your views here.

# this directs you to the developers profile page i.e. /profile/me

@login_required(login_url='/')
def profile(request):
    return render(request,'profile.html')

# this line edits the current user by pre loading their details from github i.e names and email

@login_required(login_url='/')
def edit(request):
     dev_profile = Developer.objects.get(id=request.user.pk)
     register_form = DeveloperRegistrationForm(instance=dev_profile)
     return render(request,'register.html',context= {'register_form' : register_form})


# this is where we create the user

@login_required(login_url='/')
def create(request):
    dev_profile = Developer.objects.get(id=request.user._get_pk_val)
    register_form = DeveloperRegistrationForm(request.POST or None,instance=dev_profile)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            return redirect('/profile/me/')
    return render(request,'register.html',context={'register_form' : register_form})
