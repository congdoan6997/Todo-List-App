from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm, NewTodoForm
from django.views.decorators.http import require_POST
# Create your views here.


def index(request):
    list_item = Todo.objects.order_by('id')
    form = NewTodoForm()
    return render(request, 'todo/index.html', {'list_item': list_item, 'form': form})


@require_POST
def addTodo(request):
    #form = TodoForm(request.POST)
    form = NewTodoForm(request.POST)
    if form.is_valid():
        new_todo = form.save()
        #new_todo.save()
    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')