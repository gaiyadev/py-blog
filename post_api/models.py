from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=300, unique=True)
    body = models.TextField(max_length=600)
    author = models.TextField(max_length=100, blank=True)
    isPublish = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            db_index=True, editable=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
