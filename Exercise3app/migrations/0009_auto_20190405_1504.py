# Generated by Django 2.0.13 on 2019-04-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0008_idoldetail_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idoldetail',
            name='profilepicture',
            field=models.ImageField(default='media/default.png', upload_to='gallery'),
        ),
    ]
