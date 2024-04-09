from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template.response import TemplateResponse



menu = [{'title' : "О проекте", 'url_name' : 'about'},
        {'title' : "Контакты", 'url_name' : 'contacts'},
        {'title' : "Репозиторий", 'url_name' : 'repos'},
        {'title' : "Личный кабинет", 'url_name' : 'login'}      
        ]

def index(request):
    with open('/disk/dev/VMConfigKeeper/myprojectenv/temp_cpu/myjson.json') as f:
        temp = json.load(f)
        
    data = {"CPU_temp": str(temp['CPU_temp']), 
            "GPU_temp" : str(temp['GPU_temp']), 
            "uptime" : str(temp['uptime']),
            'title': "Home",
            'title_name': "Главная",
            'menu' : menu
            }
    
    return TemplateResponse(request, "temp_cpu/index.html", context=data)
    
def about(request):

    data = {'title': "about",
            'title_name': "О проекте",
            'menu' : menu
            }
    
    return TemplateResponse(request, "temp_cpu/about.html", data)

def contacts(request):

    data = {'title': "contacts", 
            'title_name': "Контакты",
            'menu' : menu}
    
    return TemplateResponse(request, "temp_cpu/contacts.html", data)

def login(request):

    data = {'title': "login",
            'title_name': "Личный кабинет",
            'menu' : menu
            }
    
    return TemplateResponse(request, "temp_cpu/login.html", data)


def repos(request):

    data = {'title': "repos",
            'title_name': "Репозиторий",
            'menu' : menu
            }
    
    return TemplateResponse(request, "temp_cpu/repos.html", data)

