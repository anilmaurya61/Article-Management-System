# Generated by Django 4.2.17 on 2024-12-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_image_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles_images/'),
        ),
    ]
