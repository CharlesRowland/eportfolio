from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Hello World!</h1><h3>It's {now}.</h3>")

def screenprint(request):
    return render(request, "core/screenprint.html")