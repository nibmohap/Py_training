from django.db import models

# Create your models here.
class Products(models.Model):
    productCode=models.CharField(max_length=50,primary_key=True)
    productName=models.CharField(max_length=50)
    productVendor=models.CharField(max_length=50)
    productDescription=models.TextField()
    quantityInStock=models.IntegerField()
    buyPrice=models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.productName)

class Customers(models.Model):
    customerNumber=models.IntegerField(primary_key=True)
    customerName=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=20)
    email=models.EmailField()
    
    def __unicode__(self):
        return unicode(self.customerNumber)

class Orders(models.Model):
    orderNumber=models.IntegerField(primary_key=True)
    orderDate=models.DateField()
    shippedDate=models.DateField()
    status=models.CharField(max_length=15)
    customerNumber=models.ForeignKey(Customers,verbose_name="customerNumber")
    
    def __unicode__(self):
        return unicode(self.orderNumber)
    
class OrderDetails(models.Model):
    orderNumber=models.ManyToManyField(Orders)
    productCode=models.ForeignKey(Products,verbose_name="productCode")
    quantityOrderded=models.IntegerField()
    priceEach=models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.orderNumber)
    
class Payments(models.Model):
    customerNumber=models.ManyToManyField(Customers)
    checkNumber=models.IntegerField()
    paymentDate=models.DateField()
    amounts=models.FloatField()
    
    def __unicode__(self):
        return unicode(self.customerNumber)
    