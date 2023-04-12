from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # handle post requests
    if request.method == "POST":
        # handle the form
        name = request.POST['name']
        desc = request.POST['desc']
        print(name, desc)

    return render (request, 'index.html')

def product(request):
    return render (request, 'products.html')