# Generated by Django 2.0.3 on 2018-04-21 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_remove_article_entity_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_entity',
            name='filename',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
