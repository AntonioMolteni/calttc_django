# Generated by Django 4.0.5 on 2022-08-10 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_has_berkeley_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_berkeley_email',
        ),
    ]