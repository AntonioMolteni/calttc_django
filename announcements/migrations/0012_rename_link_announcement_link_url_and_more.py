# Generated by Django 4.1 on 2022-09-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0011_announcement_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='link',
            new_name='link_url',
        ),
        migrations.AddField(
            model_name='announcement',
            name='link_text',
            field=models.CharField(blank=True, default=None, max_length=80, null=True),
        ),
    ]
