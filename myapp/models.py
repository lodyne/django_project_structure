from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    heading = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    
    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.heading

