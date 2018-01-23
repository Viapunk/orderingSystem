from django.shortcuts import render
from django.http import HttpResponse
from .forms import orderingForm
from .models import *

# Create your views here.
def show_articles(request):
    if request.method == 'POST':
        productList = dict()
        for value in request.POST:
            if request.POST[value].isdigit() and request.POST[value] != '':
                productList[value] = request.POST[value]
        return render(request, 'confirmation.html', {"ordered_products" : productList})
    else:
        p = Product.objects.all()
        form = orderingForm(items=Product.objects.all())
        images = []
        productNames = []
        for item in p:
            images.append(item.image.url)
            productNames.append(item.name)
        return render(request, 'customer_template.html', {'some_form': form, 'imagesList': images, 'productnames': productNames})

    return render(request, 'customer_template.html', {'some_form': form, 'imagesList': images})

def order_confirmation(request):
    return HttpResponse(status=200)

def welcome_page(request):
    return render(request, 'hello.html')

def send_order(request):
    return HttpResponse(status=200)