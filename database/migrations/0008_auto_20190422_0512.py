# Generated by Django 2.2 on 2019-04-22 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20190422_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='image_id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user_id',
        ),
    ]
