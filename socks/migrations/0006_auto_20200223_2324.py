# Generated by Django 3.0.3 on 2020-02-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks', '0005_sock_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sock',
            name='price',
            field=models.IntegerField(default=20000),
        ),
    ]
