from django.shortcuts import render, RequestContext,redirect
from django.contrib.auth.decorators import login_required
from Register_Employer.models import Employer
from Register_Employer.forms import EmployerForm
# Create your views here.


@login_required(login_url='/emp/accounts/login/')
def emp_home(request):
    context = {'user': request.user}
    save_employer(request)
    emp = Employer.objects.get(id=request.user.id)
    if not emp.first_name:
        employer_form = EmployerForm(instance=emp)
        return render(request, 'register_emp.html', context={'user': request.user, 'employer_form': employer_form})
    return render(request,'emp_home.html', context=context)


@login_required(login_url='/emp/accounts/login/')
def register_employer(request):
    emp_details = Employer.objects.get(id=request.user._get_pk_val)
    employer_form = EmployerForm(request.POST or None, instance=emp_details)
    if request.method == 'POST':
        if employer_form.is_valid():
            employer_form.save()
            return redirect('/emp/home/')
    return render(request,'emp_home.html',context={'employer_form': employer_form})


"""
this method checks whether an employer exists in the model,
if None exists then the Employers id, username & email are saved.
"""
def save_employer(request):
    emp_id = None
    try:
        emp_id = Employer.objects.get(pk=request.user.pk)
    except:
        print('User does not exist')
    emp = Employer()
    if not emp_id:
        emp.pk = request.user.pk
        emp.user_name = request.user.username
        emp.email_address = request.user.email
        emp.is_employer = True
        emp.save()