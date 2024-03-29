# Generated by Django 4.1 on 2022-10-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('U', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('R', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], default='Friday', max_length=9)),
                ('time_slot', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('RSFField', 'RSF Field House'), ('RSFCombat', 'RSF Combatives Room')], default='RSF Field House', max_length=30)),
                ('primary_schedule', models.BooleanField(default=False)),
                ('novice_training', models.BooleanField(default=False)),
                ('intermediate_training', models.BooleanField(default=False)),
                ('advanced_training', models.BooleanField(default=False)),
                ('tournaments', models.BooleanField(default=False)),
            ],
        ),
    ]
