from django.db import models

class Course(models.Model):
    title: models.CharField = models.CharField(max_length=255)
    description: models.TextField = models.TextField()
    code: models.CharField = models.CharField(max_length=10)
    start_date: models.DateField = models.DateField()
    end_date: models.DateField = models.DateField()
    is_active: models.BooleanField = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
