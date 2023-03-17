from django.db import models

from django.db import models
from django.contrib.auth.models import User


class RecipeComment(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    subject = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    picture_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-comment_created']

    def __str__(self):
        return f'{self.id} {self.name}'