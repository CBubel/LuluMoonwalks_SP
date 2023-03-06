from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=50)
    image_path = models.CharField(max_length=255)
    current_ppu = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    fulfillment_status = models.CharField(max_length=50)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItems(models.Model):
    orderitems_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    historical_ppu = models.DecimalField(max_digits=10, decimal_places=2)

class PaymentMethod(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=50)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    is_default = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=50)
    billing_state = models.CharField(max_length=50)
    billing_zipcode = models.CharField(max_length=10)








