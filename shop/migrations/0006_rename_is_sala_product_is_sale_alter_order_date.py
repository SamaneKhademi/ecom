# Generated by Django 5.0.3 on 2024-03-17 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_star_alter_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_sala',
            new_name='is_sale',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 17, 23, 37, 27, 293309)),
        ),
    ]
