# Generated by Django 3.0.4 on 2020-03-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_sensor', '0002_auto_20200321_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Subject',
            field=models.CharField(default='Subject', max_length=75),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(default='Name', max_length=25),
        ),
    ]
