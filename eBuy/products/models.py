from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from Users.models import CustomUser  # Assuming this is your custom user model

product_category = [
    ('Education', "Education"),
    ('Electrics', "Electrics"),
    ('Midecine', "Medicine"),
    ('Fashion', "Fashion"),
    ('Grocery', "Grocery"),
    ('Kids', 'Kids'),
    ('Sport', 'Sport'),
    ('Beauty', 'Beauty'),
    ('Wearing', 'Wearing'),
    ('Religious', 'Religious'),
    ('Fruits', 'Fruits'),
    ('Vegetables', 'Vegetables'),
    ('Household', 'Household'),
    ('Toys', 'Toys'),
    ('Pet', 'Pet'),
    ('Books', 'Books'),
    ('Stationary', 'Stationary'),
    ('Furniture', 'Furniture'),
    ('Tools', 'Tools'),
    ('Automotive', 'Automotive'),
    ('Garden', 'Garden'),
]

def products_image(instance, filename):
    return f'{instance.category}/{instance.title}/{filename}'

class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = models.IntegerField()
    measure = models.CharField(max_length=50,default='kg')
    amount_sold = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=product_category)
    image = models.FileField(upload_to=products_image)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# !----------------> Order Model <-----------------!
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # not user-editable
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.first_name} {self.user.last_name} for {self.product.title}'

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        
        super().save(*args, **kwargs)
