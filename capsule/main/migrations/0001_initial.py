# Generated by Django 4.1.3 on 2022-11-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Brand_Name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SizeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200, verbose_name='Brand_Name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200, verbose_name='Type_name')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Brand_Name')),
                ('size', models.CharField(max_length=3, verbose_name='Size')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('image', models.ImageField(blank=True, default='static/img/bg.jpg', null=True, upload_to='media/productimage', verbose_name='Image')),
                ('size', models.FloatField(verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('slug', models.SlugField(unique=True)),
                ('brand_category', models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat2', to='main.brandcategory', verbose_name='Category')),
                ('size_category', models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat3', to='main.sizecategory', verbose_name='Category')),
                ('type_category', models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat1', to='main.typecategory', verbose_name='Category')),
            ],
        ),
    ]
