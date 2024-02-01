from django.db import models


# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=212)
    author = models.CharField(max_length=212)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
