# Generated by Django 4.0.1 on 2022-01-09 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ose', '0003_rename_customer_shippingaddress_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
    ]
