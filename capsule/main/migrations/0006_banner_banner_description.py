# Generated by Django 4.1.3 on 2022-11-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_price_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='banner_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]