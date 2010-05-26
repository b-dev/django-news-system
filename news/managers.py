from django.db import models

class PublishedNewsManager(models.Manager):
    def all(self):
        return self.filter()

    def filter(self, *args, **kwargs):
        return super(PublishedNewsManager, self).filter(published=True).filter(*args, **kwargs)