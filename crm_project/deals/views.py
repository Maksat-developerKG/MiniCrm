from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Deal
from .forms import DealForm

# Create your views here.

# Views For Deal
def deal_list(request):
    deals = Deal.objects.select_related('client', 'manager').all()
    return render(request=request,
                  template_name='deals/deal_list.html', 
                  context={'deals':deals})


def deal_create(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request=request,
                  template_name='deals/deal_form.html',
                  context={'form':form})


def deal_edit(requst, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if requst.method == 'POST':
        form = DealForm(requst.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('deal_list')  
    else:
        form = DealForm(instance=deal)
    return render(request=requst,
                  template_name='deals/deal_form.html',
                  context={'form':form, 'edit':True})


def deal_delete(request):
    deal = get_object_or_404
    if request.method == 'POST':
        deal.delete()
        return redirect('deal_list')
    return render(request=request,
                  template_name='deals/deal_confirm_delete.html',
                  context={'deal':deal})

