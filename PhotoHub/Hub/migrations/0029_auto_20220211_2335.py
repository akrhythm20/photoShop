# Generated by Django 3.1.6 on 2022-02-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0028_auto_20220211_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photographer',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photographer',
            name='tweeter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]