from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyProject, ContactMessage

# 1. HOMEPAGE VIEW (Only shows first 3 projects)
def index(request):
    # Slice [:3] to get only the 3 most recent projects
    projects = MyProject.objects.all().order_by('-date_added')[:3] 
    
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

    # Note: Using the path you provided in your snippet
    return render(request, 'project_app/index.html', {'projects': projects})

# 2. NEW VIEW (Shows ALL projects)
def all_projects(request):
    # Fetch ALL projects here (no slicing)
    projects = MyProject.objects.all().order_by('-date_added')
    
    # We will create this 'all_projects.html' file next
    return render(request, 'project_app/all_projects.html', {'projects': projects})