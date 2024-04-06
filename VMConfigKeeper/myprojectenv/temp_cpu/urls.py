from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="temp_cpu/about.html")),
    path('contacts/', TemplateView.as_view(template_name="temp_cpu/contacts.html"))

    ]