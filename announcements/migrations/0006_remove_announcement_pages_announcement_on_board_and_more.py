# Generated by Django 4.1 on 2022-09-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_page_remove_announcement_is_visible_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='pages',
        ),
        migrations.AddField(
            model_name='announcement',
            name='on_board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='on_home',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='on_membership_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='on_schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='on_training',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]