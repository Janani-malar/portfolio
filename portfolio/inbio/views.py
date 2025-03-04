from django.shortcuts import render, redirect
from .models import Skill, Project
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'New Message from {name}'
            body = f'You have received a new message from {name} ({email}).\n\nMessage:\n{message}'

            send_mail(
                subject,
                body,
                'jananimalarsoul@gmail.com',  # From email
                ['jananimalarsoul@gmail.com'],  # To email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Make sure 'contact' is mapped in your urls.py
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def projects_view(request):
    projects = [
        {
            "title": "Aluminum Prediction",
            "description": "A Django-based web app that predicts aluminum production based on user inputs.",
            "image": "/images/aluminum.jpg",  # Store image in static folder
            "link": "https://github.com/Janani-malar/Aluminum-Prediction-System.git",
        },
        {
            "title": "Blog Web App",
            "description": "A blogging platform built with Django and MySQL.",
            "image": "/images/blog.jpg",
            "link": "https://github.com/Janani-malar/blog_django.git",
        },
        {
            "title": "Expense Tracker",
            "description": "An application for tracking daily expenses using Django.",
            "image": "/images/expense.jpg",
            "link": "https://github.com/janani-malar/expense_tracker",
        },
        {
            "title": "Calculator",
            "description": "A simple calculator web app built with Django and JavaScript.",
            "image": "/images/calulator.jpg",
            "link": "https://github.com/Janani-malar/calculator.git",
        },
    ]

    return render(request, "projects.html", {"projects": projects})

def skills_view(request):
    skills = [
        {"name": "Python", "description": "Experienced in writing clean and efficient Python code for web applications."},
        {"name": "Django", "description": "Proficient in Django for building scalable web applications with MVC architecture."},
        {"name": "MySQL", "description": "Strong understanding of relational databases, queries, and database optimization."},
        {"name": "Web Development", "description": "Capable of designing and developing user-friendly web applications."},
        {"name": "HTML & CSS", "description": "Good at structuring web pages using HTML and styling them with CSS."},
        {"name": "Problem-Solving", "description": "Strong logical thinking and debugging skills to optimize and enhance applications."},
    ]

    return render(request, "skills.html", {"skills": skills})