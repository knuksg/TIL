from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect('todos:index')

def delete(request, todo_pk):
   todo = Todo.objects.get(pk=todo_pk)
   todo.delete()
   return redirect('todos:index')

def update(request, todo_pk):
   todo = Todo.objects.get(pk=todo_pk)
   todo.completed = not(todo.completed)
   todo.save()
   return redirect('todos:index')

def edit(request, todo_pk):
   todo = Todo.objects.get(pk=todo_pk) 
   context = {
    'todo': todo
   }
   return render(request, 'todos/edit.html', context)

def update2(request, todo_pk):
   todo = Todo.objects.get(pk=todo_pk)
   content = request.GET.get('content')
   priority = request.GET.get('priority')
   deadline = request.GET.get('deadline')
   todo.content = content
   todo.priority = priority
   todo.deadline = deadline
   todo.save()
   return redirect('todos:index')
