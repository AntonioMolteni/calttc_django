# Generated by Django 4.0.5 on 2022-08-23 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_user_wants_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='wants_membership',
            new_name='is_registered',
        ),
    ]
