from django.shortcuts import render_to_response, redirect, render,RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from Register_Developer.models import Developer
# Create your views here.


def login(request):
    return render(request,'login.html')

@login_required(login_url='/dev/')
def home(request):
    context = RequestContext(request,{'request':request,'user':request.user})
    dev_id = None
    try:
        dev_id = Developer.objects.get(pk=request.user.pk)
    except:
        print('User does not exist')
    dev = Developer()
    if not dev_id:
        dev.pk = request.user.pk
        dev.first_name = request.user.first_name
        dev.last_name = request.user.last_name
        dev.email_address = request.user.email
        dev.is_developer = True
        dev.save()
    return render_to_response('home.html',context_instance=context)

def logout(request):
    auth_logout(request)
    return redirect('/')
