# Generated by Django 4.1 on 2022-11-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimages',
            name='name',
            field=models.CharField(default='Carousel Images', max_length=14),
            preserve_default=False,
        ),
    ]