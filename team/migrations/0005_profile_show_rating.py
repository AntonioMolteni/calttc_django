# Generated by Django 4.1 on 2022-12-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_rename_a_team_profile_competitive_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='show_rating',
            field=models.BooleanField(default=False),
        ),
    ]