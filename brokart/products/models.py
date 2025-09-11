from django.db import models

# Model 
class Product(models.Model):
    LIVE = 'live'
    DELETED = 'deleted'
    DELETE_CHOICES = [
        (LIVE, 'Live'),
        (DELETED, 'Deleted'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    priority = models.IntegerField(default=0)
    delete_status = models.CharField(max_length=10, choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
