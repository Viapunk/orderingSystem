from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import orderingForm
from .models import *


def show_articles(request):
    if request.method == 'POST':
        if request.session.get('items', None):
            orderedProductList = dict()
            for value in request.POST:
                if request.POST[value].isdigit() and request.POST[value] != '':
                    orderedProductList[value] = request.POST[value]
            request.session['items'] = orderedProductList
            return render(request, 'confirmation.html', {"ordered_products": orderedProductList})
        else:
            o = Order.objects.create(productList=request.session.get('items'))
            o.save()
            request.sessios.flush()
            return redirect('orders_display')

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
    orders_list = Order.objects.all()
    return render(request, {'orders_list': orders_list})


def welcome_page(request):
    return render(request, 'hello.html')