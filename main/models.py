from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
