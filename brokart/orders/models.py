from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    LIVE = 1
    DELETED = 0
    DELETE_CHOICES = [
        (LIVE, 'Live'),
        (DELETED, 'Deleted'),
    ]
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORFER_REJECTED =4
    STATUS_CHOICES = [
        (CART_STAGE, 'Cart Stage'),
        (ORDER_CONFIRMED, 'Order Confirmed'),
        (ORDER_PROCESSED, 'Order Processed'),
        (ORDER_DELIVERED, 'Order Delivered'),
        (ORFER_REJECTED, 'Order Rejected'),
    ]
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,related_name='added_cart',null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,related_name='ordered_items',null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='cart_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
