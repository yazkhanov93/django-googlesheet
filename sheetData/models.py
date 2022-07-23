from django.db import models


class Order(models.Model):
    orderNumber = models.PositiveIntegerField(verbose_name="№")
    orderId = models.IntegerField(primary_key=True, verbose_name="заказ №")
    priceUSD = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="стоимость,$")
    priceRUB = models.DecimalField(max_digits=20, decimal_places=8, verbose_name="стоимость в руб")
    deliveryTime = models.CharField(max_length=10, verbose_name="срок поставки")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("orderNumber",)

    def __str__(self):
        return str(self.orderNumber)