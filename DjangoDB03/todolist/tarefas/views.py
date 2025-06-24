from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all().order_by('-created_at') 
    return render(request, 'tarefas/index.html', {'tarefas': tarefas})

def add_tarefa(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Tarefa.objects.create(title=title)
        return redirect('index')

def delete_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('index')

def edit_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.title = request.POST.get('title')
        tarefa.isCompleted = 'isCompleted' in request.POST
        tarefa.save()
        return redirect('index')
    return render(request, 'tarefas/edit.html', {'tarefa': tarefa})
