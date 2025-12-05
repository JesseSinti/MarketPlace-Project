from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ProductListings.models import Product
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def total(self):
        return sum(product.subtotal() for product in self.products.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity