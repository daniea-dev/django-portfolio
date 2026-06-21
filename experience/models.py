from django.db import models

class Experience(models.Model):
    TYPE_CHOICES = [
        ('academic', 'Academic'),
        ('professional', 'Professional'),
        ('project', 'Project'),
    ]

    title = models.CharField(max_length=200)
    entry_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    organization = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title