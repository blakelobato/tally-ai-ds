# Generated by Django 3.0 on 2019-12-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191217_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='high_rating_score',
        ),
        migrations.RemoveField(
            model_name='url',
            name='low_rating_score',
        ),
        migrations.RemoveField(
            model_name='url',
            name='word_phrase',
        ),
        migrations.RemoveField(
            model_name='wordlistapi',
            name='high_rating_score',
        ),
        migrations.RemoveField(
            model_name='wordlistapi',
            name='low_rating_score',
        ),
        migrations.RemoveField(
            model_name='wordlistapi',
            name='word_phrase',
        ),
    ]
