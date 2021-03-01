from django.shortcuts import render
from .models import destination
# Create your views here.
def index(request):    
    return render(request, 'index.html')

def output(request):
    total = (request.GET['total'])
    startdate = (request.GET['startdate'])
    noofquarantine = (request.GET['noofquarantine'])
    nonq = (request.GET['nonq'])
    room = (request.GET['room'])
    qt = (request.GET['qt'])

    print(total,startdate,noofquarantine,nonq)

    return render(request, 'output.html')
