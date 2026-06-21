from django.shortcuts import render, get_object_or_404
from .models import Bio

def bio_view(request, student_slug):
    bio = get_object_or_404(Bio, student_slug=student_slug)
    return render(request, 'bio/bio.html', {'bio': bio})