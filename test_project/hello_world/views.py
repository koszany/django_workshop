from django.shortcuts import render
from django.http import HttpResponse
from .models import Name

names = ['Ala', 'Bartek', 'Marcin']

def home(request):
    #return HttpResponse('<h1>Hello World</h1>')

    if(request.GET.get('namesubmit')):
        name_str = request.GET.get('namebox')
        Name(title=name_str).save()
        for name in Name.objects.all():
            print(name)
        context = {'names': [name_str]}
    else:
        context = {'names': names}
    return render(request, 'hello_world/home.html', context)

def about(request):
    return HttpResponse('<h2>About Hello World</h2>')

def request_page(request):

    return render(request,'search.html')
