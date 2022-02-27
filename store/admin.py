from django.contrib import admin
from .models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)