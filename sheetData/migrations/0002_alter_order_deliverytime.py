# Generated by Django 4.0.6 on 2022-07-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliveryTime',
            field=models.DateField(),
        ),
    ]
