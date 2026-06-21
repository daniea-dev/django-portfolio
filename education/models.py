from django.db import models

class Education(models.Model):
    student_slug = models.SlugField()
    degree_title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    board_or_university = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree_title} - {self.institution}"