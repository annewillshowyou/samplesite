from django.shortcuts import render

from .models import Bb

def index(request):
    bbs = Bb.objects.all()
    return (request, 'bboard/index.html', {'bbs':bbs})
