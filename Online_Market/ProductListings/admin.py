from django.contrib import admin
from .models import *
# Register your models here.

#registers the models to the admin page
admin.site.register(Category)
admin.site.register(Product)
