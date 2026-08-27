from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    skills = models.CharField(max_length=300)
    experience = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.title}"
