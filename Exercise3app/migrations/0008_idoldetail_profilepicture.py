# Generated by Django 2.0.13 on 2019-04-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0007_auto_20190405_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='idoldetail',
            name='profilepicture',
            field=models.ImageField(default='pictures/default.png', upload_to='pictures/'),
        ),
    ]