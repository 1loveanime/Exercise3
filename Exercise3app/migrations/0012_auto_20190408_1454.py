# Generated by Django 2.0.13 on 2019-04-08 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise3app', '0011_idolsongs_songdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='idolsongs',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='idolsongs',
            name='songtitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exercise3app.SongData'),
        ),
        migrations.AlterField(
            model_name='idolsongs',
            name='idolsinger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exercise3app.IdolDetail'),
        ),
    ]