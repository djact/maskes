# Generated by Django 3.0.7 on 2021-01-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_auto_20210102_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='ma_pod_setup',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Other', 'Other')], default=None, max_length=150),
        ),
    ]
