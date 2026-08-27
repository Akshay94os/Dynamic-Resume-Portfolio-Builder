from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume

def create_resume(request):
    if request.method == 'POST':
        resume = Resume.objects.create(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            summary=request.POST.get('summary'),
            skills=request.POST.get('skills'),
            experience=request.POST.get('experience'),
        )
        return redirect('preview_resume', pk=resume.id)
    return render(request, 'resumes/create.html')

def preview_resume(request, pk):
    resume = get_object_or_404(Resume, id=pk)
    skills_list = [s.strip() for s in resume.skills.split(',')]
    return render(request, 'resumes/preview.html', {'resume': resume, 'skills': skills_list})
