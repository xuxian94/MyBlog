from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     timestamp = models.DateTimeField()

# admin.site.register(BlogPost)

class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nickname

class BlogBody(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_type = models.CharField(max_length=50)
    blog_timestamp = models.DateTimeField()
    blog_imgurl = models.CharField(max_length=50,null=True)
    blog_author = models.CharField(max_length=20)
    def __unicode__(self):
        return self.blog_title

