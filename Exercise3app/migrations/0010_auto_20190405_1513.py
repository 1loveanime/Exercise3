# Generated by Django 2.0.13 on 2019-04-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0009_auto_20190405_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idoldetail',
            name='profilepicture',
            field=models.ImageField(blank=True, default='gallery/default.png', null=True, upload_to='gallery'),
        ),
    ]