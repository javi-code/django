from ... import models

def categorie_by_id(root, info, id):
   return models.CategoryShop.objects.get(id=id)