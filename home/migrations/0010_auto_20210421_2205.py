# Generated by Django 3.2 on 2021-04-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
