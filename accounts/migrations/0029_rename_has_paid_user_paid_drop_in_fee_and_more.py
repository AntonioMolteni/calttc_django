# Generated by Django 4.1 on 2022-09-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_remove_user_has_paid_date_user_drop_in_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='has_paid',
            new_name='paid_drop_in_fee',
        ),
        migrations.AlterField(
            model_name='user',
            name='sign_up_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]