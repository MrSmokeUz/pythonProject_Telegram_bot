from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def index(request):
    # return  HttpResponse("<h1>Test</h1>")
    return render(request, 'main/index.html')

def caesar(request):
    return render(request,'main/caesar.html')



# def about(request):
#     return render(request, 'caesar.html')
