# Generated by Django 3.1.6 on 2022-02-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0029_auto_20220211_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='query',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='photographer',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
