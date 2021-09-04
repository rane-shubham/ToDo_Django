from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField(max_length=32, null=False, blank=False)
    body = models.TextField(null=True)
    