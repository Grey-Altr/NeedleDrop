from django.db import models

# Models

# Release model
class Release(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    label = models.CharField(max_length=100)
    media_format = models.CharField(max_length=100) # convert to choice in -b dev
    cover_image = models.URLField(blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title