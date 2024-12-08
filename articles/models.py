from django.db import models
from django.conf import settings


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('published', 'Published'),
        ('rejected', 'Rejected')
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100)
    publish_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
