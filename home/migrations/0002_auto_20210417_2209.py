# Generated by Django 3.2 on 2021-04-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='desciption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
