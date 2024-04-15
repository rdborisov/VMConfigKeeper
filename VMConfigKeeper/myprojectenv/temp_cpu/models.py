from django.db import models
from django.urls import reverse


class vmconfig(models.Model):
    title = models.CharField(max_length=50)
    public_user = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    content = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='uploads_model')
    is_published = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})