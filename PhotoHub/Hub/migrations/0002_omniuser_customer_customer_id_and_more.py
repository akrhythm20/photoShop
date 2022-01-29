# Generated by Django 4.0.1 on 2022-01-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmniUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photographer',
            name='photographer_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]