# Generated by Django 3.2.13 on 2022-06-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ulc_api', '0002_auto_20220610_2148'),
    ]

    operations = [
        migrations.RenameField(
        model_name='UserProfile',
        old_name='name',
        new_name='first_name',
    ),
    ]
