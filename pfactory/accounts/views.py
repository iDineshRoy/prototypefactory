from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash

def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password1 = request.POST['password1']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        obj=User.objects.create_user(username=username, password=password1, email=email, first_name=firstname.title(), last_name=lastname.title())
        obj.save()
        update_session_auth_hash(request, request.user)
        return redirect("/")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def signin(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            context = {'message':"Login unsuccessful!"}
            return render(request, 'pages/message.html', context)
    else:
        form = UserLoginForm()
    return render(request,'login.html',{"form":form})

def changepassword(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    context = {"form":form}
    return render(request, 'changepassword.html', context)
