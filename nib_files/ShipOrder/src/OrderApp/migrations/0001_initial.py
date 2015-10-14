# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerNumber', models.IntegerField(serialize=False, primary_key=True)),
                ('customerName', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantityOrderded', models.IntegerField()),
                ('priceEach', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderNumber', models.IntegerField(serialize=False, primary_key=True)),
                ('orderDate', models.DateField()),
                ('shippedDate', models.DateField()),
                ('status', models.CharField(max_length=15)),
                ('customerNumber', models.ForeignKey(to='OrderApp.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkNumber', models.IntegerField()),
                ('paymentDate', models.DateField()),
                ('amounts', models.FloatField()),
                ('customerNumber', models.ManyToManyField(to='OrderApp.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productCode', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('productName', models.CharField(max_length=50)),
                ('productVendor', models.CharField(max_length=50)),
                ('productDescription', models.TextField()),
                ('quantityInStock', models.IntegerField()),
                ('buyPrice', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='orderNumber',
            field=models.ManyToManyField(to='OrderApp.Orders'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='productCode',
            field=models.ForeignKey(to='OrderApp.Products'),
        ),
    ]
