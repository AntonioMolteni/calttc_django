# Generated by Django 4.1 on 2022-10-01 21:43

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_user_approximate_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='approximate_rating',
            field=models.CharField(default='novice', max_length=12),
        ),
    ]