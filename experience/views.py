from django.shortcuts import render
from .models import Experience

def experience_view(request):
    experience_list = Experience.objects.all()
    return render(request, 'experience/experience.html', {'experience_list': experience_list})