from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UserProfileChange,ProfilePics

# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    diction = {'form':form, 'registered':registered}
    return render(request, 'app_login/signup.html', context=diction)

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('app_login:profile'))
    diction={'form':form}        
    return render(request,'app_login/login_page.html',context=diction)

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    diction = {}
    return render(request, 'app_login/profile.html', context=diction)
@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    diction = {'form':form}
    return render(request, 'app_login/change_profile.html', context=diction)

@login_required
def change_pass(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method=='POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            form = PasswordChangeForm(current_user)
            changed = True
    diction = {'form':form, 'changed':changed}
    return render(request, 'app_login/change_pass.html', context=diction)

@login_required
def add_pro_pic(request):
    form = ProfilePics()
    if request.method == 'POST':
        form = ProfilePics(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/add_pro_pic.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePics(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePics(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/change_pro_pic.html', context={'form':form})