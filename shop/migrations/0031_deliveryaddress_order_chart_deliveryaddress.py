# Generated by Django 4.2.4 on 2024-07-20 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_item_sold_item_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('additional_instructions', models.TextField(blank=True, null=True)),
                ('default', models.BooleanField(default=False)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.client')),
            ],
        ),
        migrations.AddField(
            model_name='order_chart',
            name='DeliveryAddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.deliveryaddress'),
        ),
    ]
