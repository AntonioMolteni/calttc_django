# Generated by Django 4.1 on 2022-09-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0012_rename_link_announcement_link_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='link_opens_in_new_tab',
            field=models.BooleanField(default=True),
        ),
    ]