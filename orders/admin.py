from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.
class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','payment','order_note','order_total','is_ordered','created_at']
    list_filter = ['user','payment','created_at']
    search_filter = ['order_number','user'] 
    list_perf_page = 20
    inlines = [OrderProductInLine]

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)