# Generated by Django 4.1 on 2022-10-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='profile_pictures')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('about', models.CharField(blank=True, max_length=150)),
                ('executive', models.BooleanField(default=False)),
                ('officer', models.BooleanField(default=False)),
                ('a_team', models.BooleanField(default=False)),
                ('b_team', models.BooleanField(default=False)),
            ],
        ),
    ]