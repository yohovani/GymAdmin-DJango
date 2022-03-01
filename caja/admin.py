from django.contrib import admin
from .models import CierreCaja
from orders.models import Order
# Register your models here.
class OrderInLine(admin.TabularInline):
    model = Order
    readonly_fields = ('user','payment','order_note','order_total','is_ordered','created_at')
    extra = 0

class CajaAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']
    list_filter = ['user','created_at']
    search_filter = ['user'] 
    list_perf_page = 20
    inlines = [OrderInLine]

admin.site.register(CierreCaja, CajaAdmin)