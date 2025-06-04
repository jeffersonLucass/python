from django.shortcuts import render
from .models import todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            todos = todo.objects.all()
            return render(request, 'home.html', {'todos': todos})
    else:
        todos = todo.objects.all()
        return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {'my_name': 'Jefferson lucas','my_age': 19}
    
    return render(request, 'about.html',context)