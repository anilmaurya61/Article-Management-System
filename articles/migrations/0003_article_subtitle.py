# Generated by Django 4.2.17 on 2024-12-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
