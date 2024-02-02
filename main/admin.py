from django.contrib import admin

from .models import Author
from .serializers import AuthorSerializer

admin.site.register(Author)


# Register your models here.
