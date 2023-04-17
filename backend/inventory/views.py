from django.shortcuts import render, HttpResponse

# Create your views here.
def inventory(request):
    return HttpResponse("This is the inventory page")