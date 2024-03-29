# Generated by Django 4.1 on 2022-10-16 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_timeslot_advanced_training_alter_timeslot_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='advanced_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='day',
            field=models.CharField(blank=True, choices=[('U', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('R', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], default='Friday', max_length=9),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='intermediate_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='location',
            field=models.CharField(blank=True, choices=[('RSFField', 'RSF Field House'), ('RSFCombat', 'RSF Combatives Room')], default='RSF Field House', max_length=30),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='novice_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='primary_schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='tournaments',
            field=models.BooleanField(default=False),
        ),
    ]
