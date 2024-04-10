from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temp_cpu.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
