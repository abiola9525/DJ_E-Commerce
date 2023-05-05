# Generated by Django 4.2 on 2023-04-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_merchant_id_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]