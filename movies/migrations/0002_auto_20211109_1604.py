# Generated by Django 3.2.9 on 2021-11-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='budget',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
