from django.utils import timezone
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    units = models.IntegerField(default=0)
    actual_unit_price = models.DecimalField(default=0, decimal_places=3, max_digits=100)
    profit_factor = models.DecimalField(default=0, decimal_places=3, max_digits=100)
    added_on = models.DateField(default=timezone.now)

    @property
    def get_unit_selling_price(self):
        return self.actual_unit_price + self.actual_unit_price * self.profit_factor


    """
    url_object = HtmlFileData()
    url_object.anchors.all()

    HtmlFileLink.objects.all(url=url_object)
     htmlfilelink_set
    """




