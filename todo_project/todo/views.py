from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(task=task)
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('todo_list')