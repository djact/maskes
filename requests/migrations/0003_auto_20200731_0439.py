# Generated by Django 3.0.7 on 2020-07-31 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20200720_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(choices=[('Signed Up', 'Signed Up'), ('Ready', 'Ready'), ('Delivered', 'Delivered')], default=None, max_length=150),
        ),
    ]
