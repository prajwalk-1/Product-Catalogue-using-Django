from django.contrib import admin

# Register your models here.

from .models import Product
from . models import Category
from . models import Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','is_published')
    list_display_links = ('id','name')
    list_filter = ('price',)
    search_fields = ('name','price')
    ordering = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)