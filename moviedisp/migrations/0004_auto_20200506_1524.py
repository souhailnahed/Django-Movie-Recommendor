# Generated by Django 3.0.6 on 2020-05-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedisp', '0003_auto_20200506_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='short_title',
            field=models.CharField(max_length=150),
        ),
    ]
