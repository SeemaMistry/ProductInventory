from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the home page")

def product(request):
    return HttpResponse("This is the products page")