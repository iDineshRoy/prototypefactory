from django.shortcuts import render, redirect
from .forms import RegistrationForm, SignUpForm, UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import User as UserProfile

def register_student(request):
    form = SignUpForm(request.POST, request.FILES or None)
    if form.is_valid():
        username = request.POST['username']
        password1 = request.POST['password1']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        is_client = False
        is_student = True
        phone = request.POST['phone']
        address = request.POST['address']
        specialization = request.POST['specialization']
        university = request.POST['university']
        photo = request.POST['photo']
        obj=User.objects.create_user(username=username, password=password1, email=email, first_name=firstname.title(), last_name=lastname.title(), is_student=is_student, is_client=is_client, phone=phone, address=address, specialization=specialization, university=university, photo=photo)
        obj.save()
        update_session_auth_hash(request, request.user)
        return redirect("/")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

def register(request):
    form = SignUpForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.is_client = False
        obj.is_student = True
        obj.first_name = (request.POST['firstname']).title()
        obj.last_name = (request.POST['lastname']).title()
        obj.save()
        return redirect("/")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

def register_client(request):
    form = SignUpForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.is_client = True
        obj.is_student = False
        obj.first_name = (request.POST['firstname']).title()
        obj.last_name = (request.POST['lastname']).title()
        obj.save()
        return redirect("/")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register_client.html', context)

def register_new(request):
    msg = None
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # form.save(commit=False)
            form.first_name = request.POST["firstname"].title()
            form.last_name = request.POST["lastname"].title()
            form.save()
            msg = "User Created"
            # update_session_auth_hash(request, request.user)
            return redirect("/")
    else:
        form = SignUpForm()
    context = {"title": "Registration Form", "form": form, "msg": msg}
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
                return redirect("profile",  request.user.id)
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

def update_student(request, id):
    obj = UserProfile.objects.get(id=request.user.id)
    user_obj = request.user
    form = SignUpForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        form.user = request.user
        obj.is_client = False
        obj.is_student = True
        obj.first_name = (request.POST['firstname']).title()
        obj.last_name = (request.POST['lastname']).title()
        obj.save()
        update_session_auth_hash(request, user_obj)
        return redirect("show_user", id)
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

@login_required
def show_user(request, id):
    user = User.objects.get(id=id)
    context = {"title": "User Profile", "user_profile": user}
    return render(request, 'user_profile.html', context)