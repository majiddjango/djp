from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    userform = UserCreationForm()
    authform = AuthenticationForm()
    context =  {
        'userform':userform,
        'authform':authform,
    }
    if request.POST and request.POST.get('log',0):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authlogin(request, user)
            return redirect('home')
        else:
            messages.error(request,'این نام کاربری وجود ندارد و یا رمز عبور اشتباه است.')
            return render(request,'accounts/login.html',context)

    elif request.POST and request.POST.get('auth',0):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authlogin(request, user)
            return redirect('home')
        else:
            errors = list(form.errors.values())
            for e in errors:
                if 'already exists.' in e[0]:
                    messages.error(request,'نام کاربری قبلا انتخاب شده است.')
                if 'password is too short' in e[0]:
                    messages.error(request,'رمز انتخابی کوتاه است. بیشتر از 8 کاراکتر انتخاب نمایید.')
            return render(request,'accounts/login.html',context)

    else:
        return render(request,'accounts/login.html',context)


@login_required
def logout(request):

    authlogout(request)
    return redirect('home')

@login_required
def change_password(request):
    context = {}
    context['title'] = 'تغییر رمز عبور'

    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            messages.error(request,'لطفا مجددا تکرار کنید.')
            form = PasswordChangeForm(user=request.user)
            context['form'] = form
            return render(request,'accounts/change.html',context)
    else:
        form = PasswordChangeForm(user=request.user)
        context['form'] = form
        return render(request,'accounts/change.html',context)
