# Generated by Django 3.0.3 on 2020-02-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks', '0006_auto_20200223_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sock',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
