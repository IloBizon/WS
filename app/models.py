from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Order(models.Model):
    product = models.ManyToManyField(Product)



