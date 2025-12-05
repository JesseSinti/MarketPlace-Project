from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    #edits the info on admin page
    class Meta: 
        #puts the categories in order by name
        ordering = ('name', )
        #changes Categorys to Categories
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        #displays the name of each category instead of object#
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #returns the name of each product instead of object #
        return self.name