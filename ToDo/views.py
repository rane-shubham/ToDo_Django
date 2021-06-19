from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(requests):
    all_todo_items = TodoItem.objects.all()
    return render(requests, 'todo.html', {'all_items':all_todo_items})

def addTodo(requests):
    new_todo_item = TodoItem(content = requests.POST['content'])
    new_todo_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(requests, todo_id):
    deleteTodo = TodoItem.objects.get(id=todo_id)
    deleteTodo.delete()
    return HttpResponseRedirect('/todo/')

# Create your views here.