'''
Created on Oct 12, 2015

@author: admin
'''
from django.http import HttpResponse 
def Hi(request):
    return HttpResponse('welcom to django application')