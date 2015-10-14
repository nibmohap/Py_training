from django.shortcuts import render
from django.http import HttpResponse
import OrderApp.models
from models import *


# Create your views here.
from django.shortcuts import render_to_response
def home(self):
    return render_to_response('Home.html')
def order(self):
    person_name='Nibedita Mohapatra'
    company='Capgemini pvt ltd'
    ship_date='19-10-2014'
    item_list=['router','switch','laptop','powerbank']
    return render_to_response('Order.html',locals())
def time(self):
    current_date='19-10-2014'
    return render_to_response('current_datetime.html',locals())
def search_form(request):
    return render_to_response('search_form.html',locals())
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        products=Products.objects.filter(productName__icontains=q)
        return render_to_response('search_result.html',{'Products':products,'query':q})
    else:
        return HttpResponse('Please submit a search form.')
    
    
