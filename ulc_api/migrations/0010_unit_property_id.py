# Generated by Django 3.2.13 on 2022-06-16 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ulc_api', '0009_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='property_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ulc_api.property'),
            preserve_default=False,
        ),
    ]
