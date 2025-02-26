from django.conf import settings
from django.db import models
from django.conf import settings
from courses.models import Course
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrolled_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    status: models.CharField = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')])
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('completed', 'Completed')]
    )
