from django.shortcuts import render, redirect
from .models import Container

def container_list(request):
    containers = Container.objects.all()
    return render(request, 'container_list.html', {'containers': containers})

def update_container_status(request, container_id):
    container = Container.objects.get(id=container_id)
    if request.method == 'POST':
        container.update_status = request.POST.get('status')
        container.save()
        return redirect('container_list')
    return render(request, 'update_container_status.html', {'container': container})
