# Generated by Django 3.2.6 on 2022-05-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_allocation_allocation_approval_asset_cash_consumables_request_scrap_service_warranty'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='returned',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
