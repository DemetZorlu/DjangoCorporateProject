# Generated by Django 3.2 on 2021-04-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Menu'), (2, 'Haber'), (3, 'Duyuru')]),
        ),
    ]
