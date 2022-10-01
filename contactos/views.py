from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactosForm
from .models import Contactos, Grupo


def home(request):
    contactos = Contactos.objects.all().order_by('nome')
    grupos = Grupo.objects.all()
    context = {
        'contactos': contactos,
        'grupos': grupos
    }
    if request.method == "POST":
        grupo = request.POST["grupo"]
        return redirect('contactos:groups')
    return render(request, 'contactos/home.html', context)

def groups(request):
    grupos = Grupo.objects.all()

    if request.method == "POST":
        grupo = request.POST["grupo"]
        contactos = Contactos.objects.filter(grupo_id=grupo)
    else:
        contactos = Contactos.objects.filter(grupo_id=1)
    context = {
        'contactos': contactos,
        'grupos': grupos
    }
    return render(request, 'contactos/groups.html', context)

def add(request):
    if request.method == "POST":
        form = ContactosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contactos:home')
    else:
        form = ContactosForm()
        context = {
            'form': form
        }
    return render(request, 'contactos/add.html', context)

def edit(request, contactos_id):
    contactos = Contactos.objects.get(pk=contactos_id)
    #criamos um formulário com base na informação do contacto
    form = ContactosForm(instance=contactos)
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ContactosForm(request.POST, request.FILES, instance=contactos)
        if form.is_valid():
            form.save()
            return redirect('contactos:home')
    return render(request, 'contactos/edit.html', context)

def delete(request, contactos_id):
    contactos = Contactos.objects.get(pk=contactos_id)
    context = {
        'contactos': contactos
    }
    contactos.delete()
    return redirect('contactos:home')
