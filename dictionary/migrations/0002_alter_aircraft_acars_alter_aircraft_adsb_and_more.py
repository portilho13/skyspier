# Generated by Django 4.2.4 on 2023-09-05 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='acars',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='adsb',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='modes',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]