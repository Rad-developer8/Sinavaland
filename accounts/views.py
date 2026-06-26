from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def register(request):
    """ثبت‌نام"""
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً استفاده شده است.')
            return redirect('accounts:register')
        
        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        if phone_number:
            user.phone_number = phone_number
            user.save()
        
        login(request, user)
        messages.success(request, 'ثبت‌نام با موفقیت انجام شد.')
        return redirect('core:home')
    
    return render(request, 'accounts/register.html')

def user_login(request):
    """ورود"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'خوش آمدید!')
            return redirect('core:home')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    """خروج"""
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید.')
    return redirect('core:home')

@login_required
def profile(request):
    """پروفایل کاربر"""
    return render(request, 'accounts/profile.html')
