# Generated by Django 4.1 on 2022-09-26 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_rename_wants_newsletter_user_opt_in_newsletter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='opt_in_newsletter',
            new_name='newsletter_subscription',
        ),
    ]