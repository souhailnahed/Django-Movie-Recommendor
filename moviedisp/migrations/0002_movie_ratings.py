# Generated by Django 3.0.6 on 2020-05-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedisp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.IntegerField(default=4),
        ),
    ]