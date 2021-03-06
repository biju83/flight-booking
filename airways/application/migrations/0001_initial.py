# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='null', max_length=50)),
                ('airport_code', models.CharField(default='null', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('airline_name', models.CharField(default='null', max_length=50)),
                ('airline_id', models.CharField(default='null', max_length=50)),
                ('source', models.CharField(default='null', max_length=50)),
                ('destination', models.CharField(default='null', max_length=50)),
                ('departure_date', models.DateTimeField(null=True)),
                ('total_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(default='null', max_length=70)),
                ('age', models.IntegerField()),
                ('passport_id', models.CharField(default='null', max_length=70)),
                ('email_id', models.EmailField(max_length=55, primary_key=True, serialize=False)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Flight')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Flight'),
        ),
    ]
