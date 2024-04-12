from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator,MinLengthValidator

# Create your models here.
STATE_CHOICES = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
)
class Customer(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   locality = models.CharField(max_length=200)
   city = models.CharField(max_length=50)
   zipcode = models.IntegerField()
   state = models.CharField(choices=STATE_CHOICES, max_length=50)

def __str__(self):
 return str(self.id)

CATEGOORY_CHOICES = (
   ('M','Mobile'),
   ('L','Laptop'),
   ('TW','Top Wear'),
   ('BW','Bottom wear'),
)

class Product(models.Model):
   title= models.CharField(max_length=100,default='')
   selling_price = models.FloatField()
   discounted_price = models.FloatField()
   description = models.TextField()
   brand = models.CharField(max_length=100)
   category = models.CharField(choices=CATEGOORY_CHOICES , max_length=2)
   product_image = models.ImageField(upload_to='productimg')

   def __str__(self):
      return str(self.id)
   
class Cart(models.Model):
      user = models.ForeignKey(User , on_delete=models.CASCADE)
      product = models.ForeignKey(Product,on_delete=models.CASCADE )
      quantity = models.PositiveBigIntegerField(default=1)

      def __str__(self):
         return str(self.id)

      @property
      def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
   ('Accepted','Accepted'),
   ('Packed','packed'),
   ('On the way','on the way'),
   ('Delivered','Delivered'),
   ('Cancel','Cancle')
)


class Orderplaced(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE )
   quentity =models.PositiveBigIntegerField(default=1)
   ordered_date = models.DateTimeField(auto_now_add=True)
   status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='pending')

