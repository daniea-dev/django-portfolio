from django.shortcuts import render
from .models import Skill

def skills_view(request):
    skills_list = Skill.objects.all()
    return render(request, 'skills/skills.html', {'skills_list': skills_list})