# Generated by Django 3.0.7 on 2020-09-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_remove_advert_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
