from django.db import models


class TypeCategory(models.Model):
    type_name = models.CharField(max_length=200, verbose_name='Type_Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.type_name


class BrandCategory(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Brand_Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.brand_name


class SizeCategory(models.Model):
    size = models.CharField(max_length=200, verbose_name='Size')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    price = models.IntegerField(verbose_name='Price')
    image = models.ImageField(upload_to='media/productimage', default='static/img/bg.jpg', null=True, blank=True,verbose_name='Image')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    type_category = models.ForeignKey(TypeCategory, on_delete=models.SET_DEFAULT, default='Common', verbose_name='Type_Category', related_name='relatedwhat1')
    brand_category = models.ForeignKey(BrandCategory, on_delete=models.SET_DEFAULT, default='Common', verbose_name='Brand_Category', related_name='relatedwhat2')
    sizes = models.ManyToManyField(SizeCategory, default='Common', verbose_name='SizeCategory', related_name='relatedwhat3')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.type_category


# need to solve small pictures of product...    additional_image = models.ImageField(upload_to='media/productimage',
# default='static/img/bg.jpg', null=True, blank=True, verbose_name='Additional-Image')


class Banner(models.Model):
    image = models.ImageField(upload_to='media/banner', default='static/def.jpg', null=True, blank=True, verbose_name='Image of Banner')
    title = models.CharField(max_length=200, null=True, blank=True)
    banner_description = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return self.title



