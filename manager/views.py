from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from django.template import loader

def sixth(request):
    customer = Customer.objects.all().values()
    template = loader.get_template('customerregistration.html')

    context = {
        'customer':customer,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
