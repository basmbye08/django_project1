#from itertools import product

from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length = 30, unique = True)
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length = 400)
    product_category = models.CharField(max_length = 100)
    product_img = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.product_id


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"



