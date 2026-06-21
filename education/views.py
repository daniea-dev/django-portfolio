from django.shortcuts import render
from .models import Education

def education_view(request):
    education_list = Education.objects.all()
    return render(request, 'education/education.html', {'education_list': education_list})