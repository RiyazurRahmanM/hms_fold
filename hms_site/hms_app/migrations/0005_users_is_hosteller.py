# Generated by Django 4.2 on 2023-04-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0004_remove_users_is_hosteller'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_hosteller',
            field=models.TextField(default='No'),
        ),
    ]
