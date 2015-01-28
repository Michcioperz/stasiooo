# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import datetime


class Entry(models.Model):
    title = models.CharField(verbose_name="tytuł", max_length=255)
    author = models.ForeignKey(User, verbose_name="autor",
                               related_name="blog_posts")
    content = tinymce_models.HTMLField(verbose_name="treść")
    publication_time = models.DateTimeField(verbose_name="czas publikacji",
                                            default=datetime.datetime.now)
    approved = models.BooleanField(verbose_name="zatwierdzone", default=False)
    pinned = models.BooleanField(verbose_name="przypięte", default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ("-pinned", "-publication_time",)
        verbose_name = "wpis"
        verbose_name_plural = "wpisy"
