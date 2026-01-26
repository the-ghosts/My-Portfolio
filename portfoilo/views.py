from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyProject, ContactMessage



def index(request):
  
    projects = MyProject.objects.all()
    
    
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
      
        messages.success(request, 'Your message has been sent. Thank you!')
        
        
        return redirect('index')

    
    return render(request, 'project_app/index.html', {'projects': projects})
# 
