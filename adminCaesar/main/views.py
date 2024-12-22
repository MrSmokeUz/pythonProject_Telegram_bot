from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def index(request):
    # return  HttpResponse("<h1>Test</h1>")
    return render(request, 'main/index.html',{'title':'Main page'})

def caesar(request):
    return render(request,'main/caesar.html')

def rsa(request):
    return render(request,'main/rsa.html')

def aes(request):
    return render(request,'main/aes.html')

def blowfish(request):
    return render(request,'main/blowfish.html')





# def about(request):
#     return render(request, 'caesar.html')
