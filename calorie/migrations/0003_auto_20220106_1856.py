# Generated by Django 3.2.7 on 2022-01-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie', '0002_auto_20220105_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='carbs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fats',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.FloatField(default=0),
        ),
    ]