# Generated by Django 4.1.3 on 2022-11-17 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_product_size_category_product_sizes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]