# Generated by Django 2.0.13 on 2019-04-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0002_auto_20190404_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idoldetail',
            name='aboutme',
            field=models.TextField(),
        ),
    ]
