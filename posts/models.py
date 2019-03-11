from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from markdown_deux import markdown
from django.utils.safestring import mark_safe

from django.db import models

# Create your models here.
class PostManager(models.Manager):
    def all(self):
        return super(PostManager, self).filter(draft=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    image = models.FileField()
    slug = models.SlugField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    # publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id':self.id})

    def get_makrdown(self):
        content = self.content
        return mark_safe(markdown(content))


