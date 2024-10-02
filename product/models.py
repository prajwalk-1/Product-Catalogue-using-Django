from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #images = models.ManyToManyField('ProductImage', related_name='products')
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)

