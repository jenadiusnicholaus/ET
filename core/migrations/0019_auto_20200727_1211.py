# Generated by Django 3.0.8 on 2020-07-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200727_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='unique_code',
            new_name='invoice_code',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, to='core.UserSubscriptions'),
        ),
    ]
