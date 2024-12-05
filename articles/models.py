
from django.db import models
from users.models import User
from django.utils import timezone


class Article(models.Model):
    # Article fields
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, choices=[
        ('tech', 'Technology'),
        ('health', 'Health'),
        ('business', 'Business'),
        ('lifestyle', 'Lifestyle'),
    ])
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=15,
        choices=[('draft', 'Draft'), ('published', 'Published'), ('rejected', 'Rejected')],
        default='draft'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
