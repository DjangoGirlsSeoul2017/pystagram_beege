from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('안녕하세요!')


def detail(request, pk):
    return HttpResponse('photo id:' + pk)
