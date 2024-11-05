# Generated by Django 5.1.2 on 2024-10-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('flow_rate', models.FloatField()),
                ('cumulative_flow_rate', models.FloatField()),
                ('water', models.FloatField()),
                ('condensate', models.FloatField()),
            ],
        ),
    ]
