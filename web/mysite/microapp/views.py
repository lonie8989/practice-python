# from django.shortcuts import render

# # Create your views here.
from datetime import datetime
from django.http import HttpResponse


def welcome(request):
    return HttpResponse('welcome to microapp')

def date(request):
  return HttpResponse('Date is ... ' + str(datetime.now()))

def page(request):
  return HttpResponse('new page')
