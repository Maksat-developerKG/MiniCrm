from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from tasks.models import Task
from deals.models import Deal
from .models import Comment
from .forms import CommentForm



@login_required
def add_comment(request, task_id=None, deal_id=None):
    task = get_object_or_404(Task, pk=task_id) if task_id else None
    deal = get_object_or_404(Deal, pk=deal_id) if deal_id else None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.deal = deal
            comment.save()


            if task:
                return redirect('task_detail', pk=task.id)
            else:
                return redirect('deal_detail', pk=deal.id)
    else:
        form = CommentForm()

    return render(request=request,
                  template_name='comments/comment_form.html',
                  context={'form':form})
            



def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = Comment.objects.filter(task=task).order_by('-created_at')
    form = CommentForm()
    return render(request=request,
                  template_name='comments/task_detail.html',
                  context={
                      'task':task,
                      'comments':comments,
                      'form':form
                  })


def deal_detail(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    comments = Comment.objects.filter(deal=deal).order_by('-created_at')
    form = CommentForm()
    return render(request=request,
                  template_name='comments/deal_detail.html',
                  context={
                      'deal':deal,
                      'comments':comments,
                      'form':form
                  })