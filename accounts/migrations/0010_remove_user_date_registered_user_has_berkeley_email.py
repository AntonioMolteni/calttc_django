# Generated by Django 4.0.5 on 2022-08-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_has_berkeley_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_registered',
        ),
        migrations.AddField(
            model_name='user',
            name='has_berkeley_email',
            field=models.BooleanField(default=False),
        ),
    ]
