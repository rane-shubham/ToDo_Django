from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def todoView(requests):
    if requests.method == 'POST':
        form = TodoForm(requests.POST or None)

        if form.is_valid():
            form.save()
            all_items = TodoItem.objects.all()
            return render(requests, 'todo.html', {'all_items':all_items})

    else:
        all_todo_items = TodoItem.objects.all()
        return render(requests, 'todo.html', {'all_items':all_todo_items})

# def addTodo(requests):
#     new_todo_item = TodoItem(content = requests.POST['content'],body = requests.POST['body'])
#     new_todo_item.save()
#     return HttpResponseRedirect('/')

def editTodo(requests, todo_id):
    if requests.method == 'POST':
        item = TodoItem.objects.get(id=todo_id)
        print(item.body, " ", item.content)

        form = TodoForm(requests.POST, instance=item)
        print(form.is_valid())

        for field in form:
            print(field.name, field.errors)
        if form.is_valid():
            form.save()

        return redirect('home')

    else:
        read_todo = TodoItem.objects.get(id=todo_id)
        return render(requests, 'todo.html', {'read_todo':read_todo})


def deleteTodo(requests, todo_id):
    delete_todo = TodoItem.objects.get(id=todo_id)
    delete_todo.delete()
    return redirect('home')

# Create your views here.
