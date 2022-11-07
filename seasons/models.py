from django.db import models

# Create your models here.

class Man(models.Model):
    title = models.CharField(max_length=210)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title