from django.shortcuts import render, get_object_or_404
from bio.models import Bio

def selector_view(request):
    students = Bio.objects.all()
    return render(request, 'home/selector.html', {'students': students})

def home_view(request, student_slug):
    bio = get_object_or_404(Bio, student_slug=student_slug)
    return render(request, 'home/home.html', {'bio': bio, 'student_slug': student_slug})