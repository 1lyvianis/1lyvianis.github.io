from week10project import views
from django.urls import path

from django.contrib import admin
urlpatterns = [
    path("", views.home),
    path("ccu410410083", views.ccu410410083_function),
    path("admin/", admin.site.urls)
]
