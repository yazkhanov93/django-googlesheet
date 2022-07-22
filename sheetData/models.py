from django.db import models


class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    priceDol = models.DecimalField(max_digits=8, decimal_places=2)
    priceRub = models.DecimalField(max_digits=8, decimal_places=2)
    deliveryTime = models.CharField(max_length=10)

    def __str__(self):
        return str(self.orderId)