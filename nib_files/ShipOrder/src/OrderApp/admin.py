from django.contrib import admin
from OrderApp.models import *


# Register your models here.
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Payments)