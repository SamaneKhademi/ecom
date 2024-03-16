# Generated by Django 5.0.3 on 2024-03-16 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_order_date_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sala',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 15, 59, 31, 751458)),
        ),
    ]
