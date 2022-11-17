from django.db import models

# Create your models here.

class Image(models.Model):
   name = models.CharField(max_length=255)
   id_file  = models.CharField(max_length=255)
   # file = models.ImageField(upload_to='images/', blank=True)
   def __str__(self):
      return self.name

class User(models.Model):
   username = models.CharField(max_length=20)
   password = models.CharField(max_length=20)
   name = models.CharField(max_length=20, default="")
   email = models.EmailField()
   phone = models.CharField(max_length=11)
   # role = models.CharField(max_length=20, choices=UserRoles.choices(), default=UserRoles.cliente)
   def __str__(self):
      return self.name

class CategoryShop(models.Model):
   name = models.CharField(max_length=20, blank=False, default=None)
   def __str__(self):
      return self.name

class Shop(models.Model):
   name = models.CharField(max_length=20, blank=False)
   urlid = models.CharField(max_length=80, blank=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   category = models.ForeignKey(CategoryShop, on_delete=models.CASCADE, null=True)
   def __str__(self):
      return self.name

class CategoryProduct(models.Model):
   name = models.CharField(max_length=20, blank=False, default=None)
   def __str__(self):
      return self.name

class Product(models.Model):
   name = models.CharField(max_length=20, blank=False)
   urlid = models.CharField(max_length=80, blank=False)
   shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
   category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)
   def __str__(self):
      return self.name