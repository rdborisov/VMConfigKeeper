from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
import json
from django.template.response import TemplateResponse
from .forms import AddPostForm
from .models import vmconfig


menu = [{'title' : "О проекте", 'url_name' : 'about'},
        {'title' : "Контакты", 'url_name' : 'contacts'},
        {'title' : "Репозиторий", 'url_name' : 'repos'},
        {'title' : "Добавить пост", 'url_name' : 'addpost'},
        {'title' : "Личный кабинет", 'url_name' : 'login'},
        
        ]

def index(request):
    with open('/disk/dev/VMConfigKeeper/myprojectenv/temp_cpu/myjson.json') as f:
        temp = json.load(f)
        
    posts = vmconfig.objects.filter(is_published=1)


    data = {"CPU_temp": str(temp['CPU_temp']), 
            "GPU_temp" : str(temp['GPU_temp']), 
            "uptime" : str(temp['uptime']),
            'title': "Home",
            'title_name': "Главная",
            'menu' : menu,
            'posts': posts,
            }
    
    return render(request, "temp_cpu/index.html", context=data)
    
def about(request):

    data = {'title': "about",
            'title_name': "О проекте",
            'menu' : menu
            }
    
    return render(request, "temp_cpu/about.html", data)

def contacts(request):

    data = {'title': "contacts", 
            'title_name': "Контакты",
            'menu' : menu}
    
    return render(request, "temp_cpu/contacts.html", data)

def login(request):

    data = {'title': "login",
            'title_name': "Личный кабинет",
            'menu' : menu
            }
    
    return render(request, "temp_cpu/login.html", data)

def uploads(file):
    with open(f"uploads/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)



def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
       #uploads(request.FILES['file_upload'])
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
        
    data = {'title': "addpost",
            'title_name': "Добавление публичной конфигурации",
            'menu' : menu,
            'form' : form
            }
    
    return render(request, "temp_cpu/addpost.html", data)


def show_post(request, post_slug):
    post = get_object_or_404(vmconfig, slug=post_slug)

    data = {
        'title' : post.title,
        'title_name': post.title,
        'menu' : menu,
        'post': post,
    }

    return render(request, 'temp_cpu/post.html', data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



def repos(request):

    data = {'title': "repos",
            'title_name': "Репозиторий",
            'menu' : menu
            }
    
    return render(request, "temp_cpu/repos.html", data)

