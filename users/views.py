from django.shortcuts import render
from .models import List

def home(request):
    users = List.objects.all
    return  render(request, 'home.html', {'users': users})


def about(request):
    my_name = 'Andrii Tugai'
    return render(request, 'about.html', {'name': my_name})
