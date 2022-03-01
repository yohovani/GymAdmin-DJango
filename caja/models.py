from django.db import models
from accounts.models import Account 
# Create your models here.

class CierreCaja(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + str(self.created_at)

