# Generated by Django 4.1 on 2022-09-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_alter_announcement_content_alter_announcement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]