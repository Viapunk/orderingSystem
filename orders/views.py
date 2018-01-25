from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import orderingForm
from .models import *
import json


def show_articles(request):
    if request.method == 'POST':
        if request.session.get('items') == None:
            orderedProductList = dict()
            for value in request.POST:
                if request.POST[value].isdigit() and request.POST[value] != '':
                    orderedProductList[value] = request.POST[value]
            request.session['items'] = json.dumps(orderedProductList)
            return render(request, 'confirmation.html', {"ordered_products": orderedProductList})
        else:
            return redirect('orders/', )
    else:
        p = Product.objects.all()
        form = orderingForm(items=Product.objects.all())
        images = []
        productNames = []
        for item in p:
            images.append(item.image.url)
            productNames.append(item.name)
        return render(request, 'customer_template.html', {'some_form': form, 'imagesList': images, 'productnames': productNames})


def orders_display(request):
    if request.session.get('items') != None:
        o = Order.objects.create(productList=request.session['items'])
        o.save()
        request.session.flush()
    orders_list = Order.objects.all()
    return render(request,'ordersDisplayPanel.html', {'orders_list': orders_list})


def welcome_page(request):
    return render(request, 'hello.html')