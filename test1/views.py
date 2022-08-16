
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import fi
# Create your views here.
import json
@csrf_exempt
def a(request):  
    data = request.body 
    f = fi()
    f.body = data
    f.save()
    return HttpResponse(data)
def b(request):
    return render(request,"index.html")