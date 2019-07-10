from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)