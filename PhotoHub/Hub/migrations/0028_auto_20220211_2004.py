# Generated by Django 3.1.6 on 2022-02-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0027_auto_20220211_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
    ]