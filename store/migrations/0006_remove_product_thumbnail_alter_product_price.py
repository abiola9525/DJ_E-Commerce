# Generated by Django 4.2 on 2023-04-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
