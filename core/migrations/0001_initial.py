# Generated by Django 3.0.8 on 2020-07-23 17:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Combination',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_title', models.CharField(blank=True, max_length=200, null=True)),
                ('unique_code', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_status', models.CharField(choices=[('p', 'Paid'), ('U', 'Unpaid')], max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('reference_id_from_ISP', models.CharField(blank=True, max_length=50, null=True)),
                ('success_type', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='provider_image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Service provider',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_price_code', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_price_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
            ],
            options={
                'verbose_name_plural': 'Subscription Price',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('sub_code', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_desc', models.CharField(blank=True, max_length=200)),
                ('sub_unit', models.PositiveIntegerField(blank=True, null=True)),
                ('sub_duration', models.CharField(blank=True, choices=[('D', 'Day'), ('W', 'Week'), ('M', 'Month'), ('Y', 'Year')], max_length=200, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('sub_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubscriptionPrice')),
            ],
            options={
                'verbose_name': 'Subscription Type',
            },
        ),
        migrations.CreateModel(
            name='USerSubscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True)),
                ('sub_status', models.CharField(blank=True, choices=[('A', 'Active'), ('E', 'expired')], max_length=20, null=True)),
                ('payment_status', models.CharField(blank=True, choices=[('p', 'Paid'), ('U', 'Unpaid')], max_length=100, null=True)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Payments')),
                ('subscription_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubscriptionType')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'subscription',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('combination_id', models.ManyToManyField(blank=True, to='core.Combinations')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id_from_ISP', models.CharField(blank=True, max_length=50, null=True)),
                ('success_type', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payments rResponse',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='service_provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ServiceProvider'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, to='core.USerSubscriptions'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='combinations',
            name='sub_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubscriptionType'),
        ),
    ]
