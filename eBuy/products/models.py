from django.contrib.auth.models import User
from django.db import models
from customerApp.models import CustomUser, CustomUserManager

# Create your models here.
 
product_category=[
  ('Education',"Education"),
  ('Electrics',"Electrics"),
  ('Midecine',"Medicine"),
  ('Fashion',"Fashion"),
  ('Grocery',"Grocery"),
  ('Kids' , 'Kids'),
  ('Sport', 'Sport'),
  ('Beauty', 'Beauty'),
  ('Wearing', 'Wearing'),
  ('Religious' , 'Religious'),
  ('Fruits' , 'Fruits'),
  ('Vegetables' , 'Vegetables'),
  ('Household' , 'Household'),
  ('Toys' , 'Toys'),
  ('Pet' , 'Pet'),
  ('Books' , 'Books'),
  ('Stationary' , 'Stationary'),
  ('Furniture' , 'Furniture'),
  ('Tools' , 'Tools'),
  ('Automotive' , 'Automotive'),
  ('Garden' , 'Garden')
  
]


def products_image(instance, filename):
  return 'users/{0}/{1}/{2}'.format(instance.owner.username, instance.title, filename)

class Products(models.Model):
   title = models.CharField(max_length=50)
   description = models.TextField(max_length=5000)
   price =models.IntegerField()
   count= models.IntegerField(default=0)
   category = models.CharField(choices=product_category)
   image=models.FileField(upload_to=products_image)
   
   
   def __str__(self):
        return self.title
   
   