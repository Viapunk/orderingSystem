from django.shortcuts import render
from orders.models import Product
from django.http import HttpResponse

# Create your views here.
def show_articles(request):
    p = Product.objects.all()
    return render(request, 'customer_template.html', {})

def hello(request):
    html = "<html><body>HelloWorld</body></html>"
    return HttpResponse(html)

def hello_template(request):
    return render(request, "hello.html")

