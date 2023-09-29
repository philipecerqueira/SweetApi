from datetime import datetime, timedelta

from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    price_sell = models.FloatField()
    price_buy = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_order = models.BooleanField(default=False)
    is_request = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def create_discount(self, discount):
        return self.price_sell - (self.price_sell * discount) / 100

    def profit(self):
        profit = self.price_sell - self.price_buy
        return (profit * 100) / self.price_buy


class Image(models.Model):
    image = models.ImageField(upload_to="products_images")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    observation = models.CharField(max_length=200)
    is_order = models.BooleanField(default=False)
    is_request = models.BooleanField(default=False)
    pickup_datetime = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.is_order and self.quantity <= 30:
            raise ValidationError(
                "For orders, the quantity must be equal to or greater than 30.")

        if self.is_order:
            if self.pickup_datetime is None:
                raise ValidationError("Pickup date is required for orders.")
            min_pickup_date = datetime.now() + timedelta(days=2)
            if self.pickup_datetime < min_pickup_date:
                raise ValidationError(
                    "Orders require a minimum pickup date of 2 days in advance.")
        elif self.is_request:
            self.pickup_datetime = datetime.now() + timedelta(hours=1)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
