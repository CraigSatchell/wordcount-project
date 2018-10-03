from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def error404(request):
    return HttpResponse('Page Not Found!')


def somepage(request):
    return HttpResponse('Some Page!!!!')


def countwords(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()
    cnt = len(wordlist)
    return render(request, 'count.html', {'cnt': cnt, 'wordlist' : wordlist})


def about(request):
    return render(request, 'about.html')