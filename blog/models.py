from django.db import models
from .sevices import *
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=128)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',blank=True,default=None)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Resizes photo if it is width or height more than 350"""
        photo = resize_photo(self.photo)
        if not self.slug:
            self.slug = slugify(self.title)
        if photo:
            self.photo = photo
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
