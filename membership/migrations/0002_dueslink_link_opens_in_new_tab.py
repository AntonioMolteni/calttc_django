# Generated by Django 4.1 on 2023-02-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dueslink',
            name='link_opens_in_new_tab',
            field=models.BooleanField(default=True),
        ),
    ]
