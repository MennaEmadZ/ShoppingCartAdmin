# Generated by Django 4.0.4 on 2022-06-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]