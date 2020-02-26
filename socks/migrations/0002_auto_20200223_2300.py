# Generated by Django 3.0.3 on 2020-02-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socks',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='socks',
            name='title',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='socks',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]