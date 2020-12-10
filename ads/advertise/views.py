from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    return render(request,'advertise/index.html')


def contact(request):
    return render(request,'advertise/contact.html')

def products(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'advertise/product.html',context)

def about(request):
    return render(request,'advertise/about.html')
