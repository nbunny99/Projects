# Generated by Django 3.0.4 on 2020-05-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_sensor', '0003_auto_20200321_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1, max_length=1)),
                ('mode', models.BooleanField(default=False)),
            ],
        ),
    ]
