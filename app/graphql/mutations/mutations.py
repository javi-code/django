import graphene
from app.models import CategoryShop
# from app.services.upload_file import UploadImage

class RegCategoryShop(graphene.Mutation):
   class Arguments:
      name = graphene.String()
   ok = graphene.Boolean()

   def mutate(root, info, name):
      shop = CategoryShop(name=name)
      shop.save()
      ok = True
      return RegCategoryShop(ok=ok)

class Mutation(graphene.ObjectType):
   reg_category_shop = RegCategoryShop.Field()
   # upload_image = UploadImage.Field()