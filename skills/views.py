from django.shortcuts import render
from .models import Skill

def skills_view(request, student_slug):
    skills_list = Skill.objects.filter(student_slug=student_slug)
    return render(request, 'skills/skills.html', {'skills_list': skills_list, 'student_slug': student_slug})