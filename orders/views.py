from django.shortcuts import render, redirect
from .forms import orderingForm
from .models import *


def show_articles(request):
    if request.method == 'POST':
        if request.session.get('items') == None:
            print(request.session.get('items'))
            orderedProductList = dict()

            for value in request.POST:
                if request.POST[value].isdigit() and request.POST[value] != '':
                    orderedProductList[value] = request.POST[value]

            request.session['items'] = orderedProductList

            print(request.session.get('items'))
            return render(request, 'confirmation.html', {"ordered_products": orderedProductList})
        else:
            print(request.POST)
            if request.POST.get('Confirmation') == 'Confirm':
                return redirect('orders/', )
            else:
                request.session.flush()
                return redirect(show_articles)
    else:
        p = Product.objects.all()
        form = orderingForm(items=Product.objects.all())
        images = []
        productNames = []

        for item in p:
            images.append(item.image.url)
            productNames.append(item.name)

        return render(request, 'customer_template.html', {'some_form': form, 'imagesList': images, 'productnames': productNames})


def orders_display_customers(request):
    print(request.session.get('items'))
    if request.method == "POST":
        order_to_update = Order.objects.get(id = request.POST['orderid'])

        if request.POST['status'] == 'Skompletowany':
            order_to_update.status = Order.READY
            order_to_update.save()

        elif request.POST['status'] == 'Odebrany':
            order_to_update.status = Order.COLLECTED
            order_to_update.save()

    if request.session.get('items') != None:
        o = Order.objects.create(productList=request.session['items'])
        o.save()
        request.session.flush()

    orders_list = Order.objects.all()
    return render(request,'ordersDisplayCustomer.html', {'orders_list': orders_list})


def orders_display(request):
    orders_list = Order.objects.all()
    request.session.flush()
    return render(request, 'ordersDisplayPanel.html', {'orders_list': orders_list})

def welcome_page(request):
    return render(request, 'hello.html')