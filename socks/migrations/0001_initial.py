# Generated by Django 3.0.2 on 2020-02-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isLeft', models.BooleanField(default=True)),
                ('isNew', models.BooleanField(default=False)),
                ('isShort', models.BooleanField(default=True)),
            ],
        ),
    ]
