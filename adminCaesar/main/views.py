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

def test(request):
    return render(request,'main/test_2.html')

def test(request):
    return render(request,'main/test_2.html')

def vigenere(request):
    return render(request,'main/vigenere.html')


def sha(request):
    return render(request,'main/sha256.html')


def des(request):
    return render(request,'main/des.html')


def trides(request):
    return render(request,'main/3des.html')

def mdfive(request):
    return render(request,'main/md5.html')


def otp(request):
    return render(request,'main/otp.html')
# def about(request):
#     return render(request, 'caesar.html')
