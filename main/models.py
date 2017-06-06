from django.db import models
from django.db.models import CharField, IntegerField, BooleanField, TextField, ForeignKey, DateTimeField
from django.contrib import admin


class Page(models.Model):
    url = CharField(max_length=100)
    title = CharField(max_length=100)
    description = TextField()
    order = IntegerField(unique=True)
    blog = BooleanField(default=False)

    def __str__(self):
        return self.url


class Post(models.Model):
    title = CharField(max_length=100)
    body = TextField()
    visible = BooleanField(default=False)
    page = ForeignKey('Page')
    order = IntegerField(unique=True, blank=True)
    posted_time = DateTimeField(blank=True, null=True)
    modified_time = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


admin.site.register(Page)
admin.site.register(Post)
