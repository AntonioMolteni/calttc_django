# Generated by Django 4.1 on 2023-04-07 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_remove_user_approximate_rating_user_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_checked_in',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_drop_in_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='paid_drop_in_fee',
        ),
    ]
