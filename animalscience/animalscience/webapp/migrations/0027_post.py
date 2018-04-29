# Generated by Django 2.0.3 on 2018-04-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(default='none', max_length=30)),
                ('author', models.CharField(default='none', max_length=30)),
                ('description', models.CharField(default='none', max_length=30)),
            ],
        ),
    ]
