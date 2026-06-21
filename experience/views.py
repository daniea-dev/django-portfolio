from django.shortcuts import render
from .models import Experience

def experience_view(request, student_slug):
    experience_list = Experience.objects.filter(student_slug=student_slug)
    return render(request, 'experience/experience.html', {'experience_list': experience_list})