from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.select_related('assigned_to').all()
    return render(request=request,
                  template_name='tasks/task_list.html',
                  context={'tasks':tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request=request,
                  template_name='tasks/task_form.html', 
                  context={'form':form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request=request,
                  template_name='tasks/task_form.html',
                  context={'form':form, 'edit':True})

        

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request=request,
                  template_name='tasks/task_confirm_delete.html',
                  context={'task':task})


