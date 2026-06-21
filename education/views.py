from django.shortcuts import render
from .models import Education

def education_view(request, student_slug):
    education_list = Education.objects.filter(student_slug=student_slug)
    return render(request, 'education/education.html', {'education_list': education_list, 'student_slug': student_slug})