from cgitb import lookup
from dataclasses import fields
from graphene_django import DjangoObjectType

from ... import models

class ProductType(DjangoObjectType):
   class Meta:
      model = models.Product
      # exclude_fields = ('user', )

class ShopType(DjangoObjectType):
   class Meta:
      model = models.Shop
      exclude_fields = ('user', )

class UserType(DjangoObjectType):
   class Meta:
      model = models.User
      exclude_fields = ('password',)
      

class CategoryShopType(DjangoObjectType):
   class Meta:
      model = models.CategoryShop

class CategoryProductType(DjangoObjectType):
   class Meta:
      model = models.CategoryProduct

class ImagesType(DjangoObjectType):
   class Meta:
      model = models.Image