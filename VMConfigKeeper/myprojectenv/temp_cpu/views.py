from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
    with open('/disk/dev/VMConfigKeeper/myprojectenv/temp_cpu/myjson.json') as f:
        temp = json.load(f)
    #CPU_temp = str(temp['CPU_temp'])
    data = {"CPU_temp": str(temp['CPU_temp']), "GPU_temp" : str(temp['GPU_temp']), "uptime" : str(temp['uptime'])}
    return TemplateResponse(request, "temp_cpu/home.html", data)
    
#def about(request):
 #   return HttpResponse("<h2>Главная</h2>")

