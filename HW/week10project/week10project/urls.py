from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu410410083', views.ccu410410083_function)
]
