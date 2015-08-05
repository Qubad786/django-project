from django.db import models
from django.utils import timezone


class Sales(models.Model):
    user = models.ForeignKey('user.User', related_name='sales')
    product = models.ForeignKey('products.Products', related_name='sales')
    profit = models.DecimalField(default=0, decimal_places=3, max_digits=100)
    units = models.IntegerField(default=0)
    sold_on = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.profit = (self.product.get_unit_selling_price - self.product.actual_unit_price) * self.units
        super(Sales, self).save(*args, **kwargs)

    @staticmethod
    def autocomplete_search_fields():
        return ("user__username", "user__email", "product__name", "product__kind")




