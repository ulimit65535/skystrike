from django.db import models

# Create your models here.
class Source(models.Model):

    """
    采集数据来源
    """
    name = models.CharField(max_length=20, unique=True)
    url = models.URLField()

class Article(models.Model):

    """采集到的文章"""
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.CharField(max_length=20, null=True)
    posted_time = models.DateTimeField(null=True, blank=True)
    collected_time = models.DateTimeField()
    url = models.URLField(unique=True)
    first_pic_url = models.URLField(null=True)
    source = models.ForeignKey(Source)

