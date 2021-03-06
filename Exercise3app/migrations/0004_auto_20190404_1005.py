# Generated by Django 2.0.13 on 2019-04-04 02:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0003_auto_20190404_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idoldetail',
            name='name',
        ),
        migrations.AddField(
            model_name='idoldetail',
            name='namefirst',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='idoldetail',
            name='namelast',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='idoldetail',
            name='namemiddle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='idoldetail',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
