# Generated by Django 3.0.3 on 2020-04-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0008_remove_experiment_fact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='settings_hash',
            field=models.TextField(help_text='md5 hash of key sorted normalized machine, settings, p, dictionary'),
        ),
    ]
