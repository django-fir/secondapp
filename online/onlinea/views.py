from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def time(request):
    date = datetime.datetime.now()
    return HttpResponse(f'<h1>The Current Working Time Is : {date}</h1>')
