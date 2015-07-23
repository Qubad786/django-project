from django.db import models
from django.db.models import Sum
from django.db.models.manager import Manager
from django.utils import timezone


class ReservationsManager(Manager):

    # noinspection PyMethodMayBeStatic
    def get_top_five_reserved_products(self):

        """
        SQL Query: Top 5 reserved products
        select product_name, type, brand, sum(ordered_units) as units from
        (select products_products.product_name, products_products.type, products_products.brand,
         reservations_reservations.ordered_units from products_products,reservations_reservations
         where products_products.id = reservations_reservations.product_id) AS top_reservations
         group by product_name,brand,type order by units desc limit 5

        """

        top_five_reserved_products = Reservations.objects\
            .values('product__product_name', 'product__type', 'product__brand')\
            .annotate(units=Sum('ordered_units')) \
            .order_by('-units')[:5]
        return top_five_reserved_products

    # noinspection PyMethodMayBeStatic
    def get_top_five_customers_based_on_reservations(self):

        """
        SQL Query: TOP 5 Customers
        select username, email, sum(ordered_units) as units from
        (select user_user.username, user_user.email,
        reservations_reservations.ordered_units from user_user,reservations_reservations
        where user_user.id = reservations_reservations.user_id) AS top_reservations
        group by username,email order by units desc limit 5

        """

        top_five_customers_based_on_reservations = Reservations.objects\
            .values('user__username', 'user__email') \
            .annotate(units=Sum('ordered_units')) \
            .order_by('-units')[:5]
        return top_five_customers_based_on_reservations


class Reservations(models.Model):
    user = models.ForeignKey('user.User', related_name='reservations')
    product = models.ForeignKey('products.Products', related_name='reservations')
    price = models.DecimalField(default=0, decimal_places=3, max_digits=100)
    ordered_units = models.IntegerField(default=0)
    order_date = models.DateField(default=timezone.now)

    objects = ReservationsManager()

    def save(self, *args, **kwargs):
        self.price = self.product.get_unit_selling_price
        self.product.units -= self.ordered_units
        self.product.save()
        super(Reservations, self).save(*args, **kwargs)




