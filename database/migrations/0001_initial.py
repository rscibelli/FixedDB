# Generated by Django 2.2 on 2019-04-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibility', models.BooleanField(default=False, null=True)),
                ('invited_by', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('points', models.IntegerField(null=True)),
                ('user_type', models.CharField(max_length=50, null=True)),
                ('login_time', models.CharField(max_length=50, null=True)),
                ('logout_time', models.CharField(max_length=50, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_verified', models.BooleanField(default=True, null=True)),
                ('birthday', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
