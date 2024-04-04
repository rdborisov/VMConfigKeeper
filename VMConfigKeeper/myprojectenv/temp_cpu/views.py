from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.

def index(request):
    with open('/disk/dev/VMConfigKeeper/myprojectenv/temp_cpu/myjson.json') as f:
        temp = json.load(f)
    return HttpResponse(f"<h3>CPU_temp: {str(temp['CPU_temp'])}</h3>\n<h3>GPU_temp: {str(temp['GPU_temp'])}</h3>\n<h3>uptime: {str(temp['uptime'])}</h3>")
    
                          

