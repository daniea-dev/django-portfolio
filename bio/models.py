from django.db import models

class Bio(models.Model):
    student_slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name