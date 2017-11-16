from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Source(models.Model):

    """
    采集数据来源
    """
    name = models.CharField(max_length=20, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('warehouse:source', kwargs={'pk': self.pk})

class Article(models.Model):

    """采集到的文章"""
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.CharField(max_length=20, null=True)
    posted_time = models.DateTimeField(null=False, blank=False, unique=True)
    collected_time = models.DateTimeField()
    url = models.URLField(null=False, blank=False)
    first_pic_url = models.URLField(default=None)
    source = models.ForeignKey(Source)

    def get_absolute_url(self):
        return reverse('warehouse:article', kwargs={'pk': self.pk})

