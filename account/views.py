from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages

def registration(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request,'you have been registered successfully waithing for redirect')
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'account/signup.html',{'user_form':user_form})

def dashboard(request):
    return render(request,'account/dashboard.html')
