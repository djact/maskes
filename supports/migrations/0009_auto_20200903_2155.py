# Generated by Django 3.0.7 on 2020-09-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supports', '0008_auto_20200831_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='food_restrictions',
            field=models.TextField(blank=True, default=None, max_length=1024),
        ),
        migrations.AlterField(
            model_name='request',
            name='special_info',
            field=models.TextField(blank=True, max_length=2048),
        ),
    ]
