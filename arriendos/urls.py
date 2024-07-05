from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app.urls')),
]