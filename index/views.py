from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('voce esta no index do app')
