# Generated by Django 5.0.1 on 2024-04-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_requires_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='requires_shipping',
        ),
    ]
