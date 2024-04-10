from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('file/', views.repos, name='repos'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('addpost/', views.addpost, name='addpost'),
    ]