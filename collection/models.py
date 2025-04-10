from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Models

# Release model
class Release(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    media_format = models.CharField(max_length=100) # convert to choice in -b dev
    cover_image = models.URLField(blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('release-detail', kwargs={'pk': self.pk})