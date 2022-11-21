from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'phone.html', {})


def confirm(request):
    user = request.GET['UserName']
    mail = request.GET['UserMail']
    return HttpResponse(user + ', 你輸入的email是' + mail)


def ccu410410083_function(request):
    user = request.GET['UserName']
    mail = request.GET['UserMail']
    return HttpResponse('Succcccccess! 成功啦!' + '\n' + user + ', 你輸入的email是' + mail)
