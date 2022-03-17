from django.db import models
from accounts.models import Account
from store.models import Product
from caja.models import CierreCaja
# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    payment_paid = models.FloatField(default=0)
    cambio = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_method

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    cierre_caja = models.ForeignKey(CierreCaja, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.user.first_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name