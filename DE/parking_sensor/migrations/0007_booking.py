# Generated by Django 3.0.4 on 2020-06-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_sensor', '0006_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_no', models.IntegerField()),
            ],
        ),
    ]
