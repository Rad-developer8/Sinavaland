from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    """صفحه اصلی"""
    return render(request, 'core/home.html')

def contact(request):
    """تماس با ما"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, 'پیام شما با موفقیت ارسال شد.')
        return redirect('contact')
    
    return render(request, 'core/contact.html')
