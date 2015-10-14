'''
Created on Oct 13, 2015

@author: admin
'''
from OrderApp.models import *

#Products.objects.create(productCode='77',productName='pant',productVendor='GKTCS',productDescription='sold',quantityInStock='2',buyPrice='900')

p1=Products.objects.get(productCode='77')
print "its name",p1.productName
print "its vendor",p1.productVendor
print "its desc",p1.productDescription
