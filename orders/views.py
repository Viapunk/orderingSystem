from django.shortcuts import render
from orders.models import Product
from django.http import HttpResponse
from .forms import orderingForm


# Create your views here.
def show_articles(request):
    p = Product.objects.all()
    form = orderingForm(items=Product.objects.all())
    images = []
    for item in p:
        images.append(item.image.url)

    return render(request, 'customer_template.html', {'some_form': form, 'imagesList': images})

def order_confirmation(request):
    return HttpResponse(status=200)

def welcome_page(request):
    return render(request, 'hello.html')
