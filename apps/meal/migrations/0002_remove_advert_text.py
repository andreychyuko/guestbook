# Generated by Django 3.0.7 on 2020-09-22 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='text',
        ),
    ]
