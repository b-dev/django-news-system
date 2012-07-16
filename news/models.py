# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from news.managers import PublishedNewsManager

class News(models.Model):
    pubs_objects = PublishedNewsManager()

    # Optional
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255) 
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published = models.BooleanField(default=False)

    # Automatic
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/news/%s/" % self.slug

    class Meta:
        ordering = ['-created_at']
