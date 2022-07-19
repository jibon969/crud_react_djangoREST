from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
