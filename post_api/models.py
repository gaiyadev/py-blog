from django.db import models

# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=6000)
   # created_at = models.DateField(auto_created=True, blank=True, default=True)


def __str__(self):
    return self.title
