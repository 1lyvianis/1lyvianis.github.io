from week10project.models import User
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'phone.html', {})


def ccu410410083_function(request):
    user = request.GET['UserName']
    mail = request.GET['UserMail']
    suggestion = request.GET['User_suggestion']
    u = User(username=user, email=mail, textarea=suggestion)
    u.save()
    return render(request, 'users_template.html', {'users_list': User.objects.all()})
