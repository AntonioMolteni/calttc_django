# Generated by Django 4.1 on 2022-09-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_rename_advanced_sign_up_date_user_sign_up_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_checked_in',
            field=models.BooleanField(default=False),
        ),
    ]