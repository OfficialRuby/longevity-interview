# Generated by Django 4.0.6 on 2022-07-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='length',
            new_name='height',
        ),
        migrations.AlterField(
            model_name='parameter',
            name='measure_instrument',
            field=models.CharField(choices=[('metric', 'Metric'), ('imperial', 'Imperial'), ('custom', 'Custom')], max_length=30),
        ),
    ]
