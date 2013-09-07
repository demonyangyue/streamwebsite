from django.db import models

# Create your models here.

class FileSource(models.Model):
    name = models.CharField(max_length = 15)

    def __unicode__(self):
        return self.name

