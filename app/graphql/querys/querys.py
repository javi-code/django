from unicodedata import category
import graphene
from graphene_django import DjangoListField

from app.models import CategoryShop

from .resolvers import (
   categorie_by_id,
)

from .types import (
   ProductType,
   UserType,
   ShopType,
   CategoryShopType,
   CategoryProductType,
   ImagesType
)

class Query(graphene.ObjectType):
   users    = DjangoListField(UserType)
   shops    = DjangoListField(ShopType)
   products = DjangoListField(ProductType)
   categorysShops = DjangoListField(CategoryShopType)
   categorysProducts = DjangoListField(CategoryProductType)
   images = DjangoListField(ImagesType)

   categorie_shop  = graphene.Field(CategoryShopType, id=graphene.Int(), resolver=categorie_by_id)