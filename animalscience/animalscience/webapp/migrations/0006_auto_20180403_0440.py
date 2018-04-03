# Generated by Django 2.0.3 on 2018-04-03 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20180403_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_author_rel',
            name='article_id_fk',
        ),
        migrations.RemoveField(
            model_name='article_author_rel',
            name='author_id_fk',
        ),
        migrations.RemoveField(
            model_name='article_key_rel',
            name='article_id_fk',
        ),
        migrations.RemoveField(
            model_name='article_key_rel',
            name='key_id_fk',
        ),
        migrations.AddField(
            model_name='article_entity',
            name='author_fk',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.author_entity'),
        ),
        migrations.AddField(
            model_name='article_entity',
            name='key_fk',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.key_entity'),
        ),
        migrations.DeleteModel(
            name='article_author_rel',
        ),
        migrations.DeleteModel(
            name='article_key_rel',
        ),
    ]
