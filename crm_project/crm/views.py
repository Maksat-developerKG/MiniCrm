from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Client
from .forms import ClientForm

# View for Clients
def client_list(request):
    clients = Client.objects.all()
    return render(request=request, 
                  template_name='crm/client_list.html', 
                  context={'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        
    else:
        form = ClientForm()
    return render(request=request,
                  template_name='crm/client_form.html',
                  context={'form':form})



def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request=request,
                  template_name='crm/client_form.html',
                  context={'form':form, 'edit':True})



def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request=request,
                  template_name='crm/client_confirm_delete.html',
                  context={'client':client})



