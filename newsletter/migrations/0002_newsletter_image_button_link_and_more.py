# Generated by Django 4.1 on 2023-03-07 12:12

from django.db import migrations, models
import newsletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='image_button_link',
            field=models.URLField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='unsubscribe_link',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='gmail_csv',
            field=models.FileField(blank=True, upload_to=newsletter.models.upload_location),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='test_user_email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]