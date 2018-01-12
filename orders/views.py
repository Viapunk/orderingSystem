from django.shortcuts import render
from orders.models import Product

# Create your views here.
def show_articles(request):
    p = Product.objects.all()
    return render(request, 'customer_template.py', {})



