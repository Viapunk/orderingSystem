from django.shortcuts import render
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

def send_order(request):
    return HttpRequest