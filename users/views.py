from django.shortcuts import render

def home(request):
    return  render(request, 'home.html', {})


def about(request):
    my_name = 'Andrii Tugai'
    return render(request, 'about.html', {'name': my_name})
