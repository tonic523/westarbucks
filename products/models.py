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
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=100, blank=True)
    english_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    nutrition_id = models.ForeignKey('Nutritions', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'products'

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 6, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    saturated_fat_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

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

class Allergy_products(models.Model):
    allergy_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'