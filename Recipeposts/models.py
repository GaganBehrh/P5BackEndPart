
from django.db import models
from django.contrib.auth.models import User


class RecipePost(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_2017', '2017'),
        ('bran', 'Bran'),
        ('spoon', 'Spoon'),
        ('fork', 'Fork'),
        ('bowl', 'Bowl'),
        ('plate', 'Plate'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    matter = models.TextField(blank=True)
    pic = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq'
    )
    pic_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.name}'