# Generated by Django 4.2 on 2023-07-04 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0005_rename_order_id_orderline_order_alter_order_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 16, 28, 2, 523376)),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 16, 28, 2, 523376)),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 16, 28, 2, 523376)),
        ),
    ]
