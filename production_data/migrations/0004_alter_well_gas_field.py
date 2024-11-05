# Generated by Django 5.1.2 on 2024-11-04 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_data', '0003_gasfield_well_gas_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='gas_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='production_data.gasfield'),
        ),
    ]