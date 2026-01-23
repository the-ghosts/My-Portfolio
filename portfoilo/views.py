from django.shortcuts import render, redirect
from .models import MyProject, ContactMessage
from django.contrib import messages

def home(request):
    portfolio = MyProject.objects.all().order_by('-date_added')
    return render(request, 'project_app/index.html', {'projects': portfolio})


def index(request):
    projects = MyProject.objects.all()
    
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Show a success message
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('index') # Reload the page

    return render(request, 'index.html', {'projects': projects})
# Create your views here.
