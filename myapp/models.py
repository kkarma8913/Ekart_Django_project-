from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    pro_id = models.CharField(max_length=20,primary_key=True)
    pro_title = models.CharField(max_length=100)    
    pro_price = models.PositiveIntegerField()
    pro_category = models.ForeignKey(Category,on_delete=models.CASCADE) # obj of category
    pro_image = models.ImageField(upload_to='product_image',null=True,blank=True)
    pro_rating = models.IntegerField()
    pro_description = models.TextField()

    def __str__(self):
        return self.pro_title


gender_choice = (('Male','Male'),('Female','Female'),('Other','Other'))
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=gender_choice)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
payment_mode_choice = (('COD','COD'),('Credit card','Credit card'),('Debit card','Debit card'),('UPI','UPI'))    
status_choice = (('Pending','Pending'),('Approved','Approved'))


class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0) 
    total_price = models.IntegerField()

    def __str__(self):
        return self.customer.name 
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    payment_mode = models.CharField(max_length=50,choices=payment_mode_choice)  
    total_price = models.IntegerField()
    order_date = models.DateField()
    order_status = models.CharField(max_length=50,choices=status_choice,default="Pending")

    def __str__(self):
        return self.customer.name     

