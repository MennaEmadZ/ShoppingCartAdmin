# Generated by Django 4.0.4 on 2022-05-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
    ]
