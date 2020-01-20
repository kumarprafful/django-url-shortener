from django.db import models

# Create your models here.
class URLs(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    long_url = models.URLField(max_length=255, unique=True)
    short_url = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_id + ' - ' +  self.long_url
    
    class Meta:
        verbose_name = 'URL'