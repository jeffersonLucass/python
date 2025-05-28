from django.shortcuts import render
from .models import todo

def home(request):
    todos = todo.objects.all()
    return render(request, 'home.html',{'todos':todos})


def about(request):
    context = {'my_name': 'Jefferson lucas','my_age': 19}
    
    return render(request, 'about.html',context)