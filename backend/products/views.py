from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    context = {'success': False}
    # handle post requests
    if request.method == "POST":
        # handle the form
        name = request.POST['name']
        desc = request.POST['desc']
        product = Product(name=name, desc=desc)
        context = {'success': True}
        product.save()

    return render (request, 'index.html', context)

def product(request):
    # retrieve all the products
    allProducts = Product.objects.all()
    context = {'products': allProducts}

    return render (request, 'products.html', context)