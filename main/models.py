from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


