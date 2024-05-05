from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImageUrl(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image_url = models.URLField()
    alt = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.product} - {self.product.category}'
