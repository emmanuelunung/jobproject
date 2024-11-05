from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import Application
from .models import Job


# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        resume = request.FILES['resume']
        application = Application(job=job, applicant=request.user, resume=resume)
        application.save()
        return redirect('job_list')
    return render(request, 'apply.html', {'job': job})



def application_list(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'application_list.html', {'applications': applications})
