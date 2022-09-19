# Generated by Django 4.1.1 on 2022-09-18 13:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldborder',
            name='iso3',
            field=models.CharField(max_length=3, null=True, verbose_name='3 Digit ISO'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='region',
            field=models.IntegerField(null=True, verbose_name='Region Code'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='subregion',
            field=models.IntegerField(null=True, verbose_name='Sub Region Code'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='un',
            field=models.IntegerField(null=True, verbose_name='united Nation Code'),
        ),
    ]
