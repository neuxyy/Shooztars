# Generated by Django 5.0.1 on 2024-04-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_product_digital_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='requires_shipping',
            field=models.BooleanField(default=False),
        ),
    ]
