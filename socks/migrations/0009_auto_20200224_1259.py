# Generated by Django 3.0.3 on 2020-02-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks', '0008_auto_20200224_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sock',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]