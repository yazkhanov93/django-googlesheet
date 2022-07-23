# Generated by Django 4.0.6 on 2022-07-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetData', '0004_rename_pricedol_order_priceusd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='priceRub',
        ),
        migrations.AddField(
            model_name='order',
            name='orderNumber',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='priceRUB',
            field=models.DecimalField(decimal_places=8, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]