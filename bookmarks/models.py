# Load the siteconf module
from django.conf import settings
from django.utils.importlib import import_module
SITECONF_MODULE = getattr(settings, 'AUTOLOAD_SITECONF', settings.ROOT_URLCONF)
import_module(SITECONF_MODULE)


from django.db import models
class PressRelease(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title

class Link(models.Model):
    url = models.URLField(unique=True)
    def __str__(self):
        return self.url
    class Admin:
        pass
    
