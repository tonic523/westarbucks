from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    ko_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 6, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    saturated_fat_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    product_name = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length = 2000)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

class Allergies_products(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'
