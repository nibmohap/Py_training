# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='productCode',
            field=models.ForeignKey(verbose_name=b'productCode', to='OrderApp.Products'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customerNumber',
            field=models.ForeignKey(verbose_name=b'customerNumber', to='OrderApp.Customers'),
        ),
    ]
