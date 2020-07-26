# Generated by Django 3.0.8 on 2020-07-24 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200724_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usersubscriptions',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
