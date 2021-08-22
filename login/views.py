from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from .forms import SignUpForms,EditProfileForm,ChangeUserPassword

# Create your views here.

def home(request):
    return render(request,'login/home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have being login'))
            return redirect('home')
        else:
            messages.success(request,('Error Loging in'))
            return redirect('login')
    else:
        return render(request,'login/login_.html')


def logout_user(request):
    logout(request)
    messages.success(request,('You have being logout'))

    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)

            login(request,user)
            messages.success(request,'You have registered')
            return redirect('home')

    else:
        form = SignUpForms()


    context = {'form':form}

    return render(request,'login/register.html',context)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'You have succefully edit your profile')
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)


    context = {'form':form}

    return render(request,'login/edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = ChangeUserPassword(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'You have change your password')
            return redirect('home')

    else:
        form = ChangeUserPassword(user=request.user)


    context = {'form':form}

    return render(request,'login/change_password.html',context)