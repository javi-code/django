from django.contrib import admin

# Register your models here.
from .models import CategoryShop, Product, Shop, User, CategoryProduct, Image

class UserAdmin(admin.ModelAdmin):
   list_display = ('username', 'name', 'email', 'phone','role')
   search_fields = ('username', 'name', 'email', 'phone')

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'shop', 'category')
   list_filter = ['category']
   search_fields = ['name']

admin.site.register(Image)
# admin.site.register(User, UserAdmin)
admin.site.register(Shop)
admin.site.register(CategoryShop)
admin.site.register(CategoryProduct)
admin.site.register(Product, ProductAdmin)