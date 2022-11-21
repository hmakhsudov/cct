# Generated by Django 4.1.3 on 2022-11-17 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typecategory',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='typecategory',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand_category',
            field=models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat2', to='main.brandcategory', verbose_name='Brand_Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_category',
            field=models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat3', to='main.sizecategory', verbose_name='SizeCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_category',
            field=models.ForeignKey(default='Common', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='relatedwhat1', to='main.typecategory', verbose_name='Type_Category'),
        ),
        migrations.AlterField(
            model_name='typecategory',
            name='type_name',
            field=models.CharField(max_length=200, verbose_name='Type_Name'),
        ),
    ]
