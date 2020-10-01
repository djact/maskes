# Generated by Django 3.0.7 on 2020-09-15 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0009_auto_20200903_2155'),
        ('funds', '0006_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='reimbursement',
        ),
        migrations.AddField(
            model_name='donation',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.Request', verbose_name='Request ID'),
            preserve_default=False,
        ),
    ]
