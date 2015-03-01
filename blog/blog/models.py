from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
#    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    #category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField('Tag', related_name = 'blogs', blank = True)
    
    def __str__(self):
        return self.title

#    @permalink
#    def get_absolute_url(self):
#        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Tag(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.label