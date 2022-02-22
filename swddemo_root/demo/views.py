from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<hi>Hello World</hi>")
# Create your views here.
