from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Inmueble, Perfil, Region, Comuna, Contact
from .forms import UserForm, PerfilForm, InmuebleForm, ContactForm

@login_required(login_url='/login/')
def index(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    inmuebles = Inmueble.objects.all()

    if region_id:
        inmuebles = inmuebles.filter(id_region=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(id_comuna=comuna_id)
    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas
    }
    return render(request, 'index.html', context)
    

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/profile/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
        
@login_required(login_url='/login/')
def profile(request):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)
    tipo = perfil.tipo_usuario.tipo

    context = {
        'perfil': perfil,
        'tipo': tipo
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/login/')
def register_profile(request):
    usuario = request.user
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = usuario
            perfil.correo = usuario.email
            perfil.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = PerfilForm()
    
    context = {
        'form': form,
        'title': 'Crear perfil'
    }
    return render(request, 'register_profile.html', context)

@login_required(login_url='/login/')
def update_profile(request):
    usuario = request.user  
    perfil = get_object_or_404(Perfil, usuario=usuario)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = PerfilForm(instance=perfil)
    
    context = {
        'form': form,
        'title': 'Actualizar Perfil'
    }
    return render(request, 'register_profile.html', context)

@login_required(login_url='/login/')
def register_inmueble(request, username):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.id_usuario = usuario
            inmueble.save()
            return HttpResponseRedirect('/inmuebles/')
    else:
        form = InmuebleForm()
    
    context = {
        'form': form,
        'tipo': tipo,
        'title': 'Registrar Inmueble'
    }
    return render(request, 'register_inmueble.html', context)

@login_required(login_url='/login/')
def get_inmuebles(request):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    inmuebles = Inmueble.objects.filter(id_usuario=usuario)
    
    context = {
        'inmuebles': inmuebles,
        'tipo': tipo,
        'title': 'Registrar Inmueble'
    }
    return render(request, 'inmuebles.html', context)

@login_required(login_url='/login/')
def update_inmueble(request, pk):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    inmueble = get_object_or_404(Inmueble, pk=pk)

    if request.method == "POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inmuebles/')
    else:
        form = InmuebleForm(instance=inmueble)
    
    context = {
        'form': form,
        'title': 'Editar Inmueble',
        'tipo': tipo
    }
    return render(request, 'register_inmueble.html', context)

@login_required(login_url='/login/')
def contact(request, id):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.nombre_inmueble = inmueble.nombre_inmueble
            contact.arrendador = inmueble.id_usuario
            contact.save()
            return HttpResponseRedirect('/home/')
    
    form = ContactForm()
    context = {
        'form': form,
        'title': 'Contacta al Propietario',
        'tipo': tipo
    }
    return render(request, 'contact.html', context)

@login_required(login_url='/login/')
def messages(request):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    messages = Contact.objects.filter(arrendador=usuario)
    
    context = {
        'messages': messages,
        'tipo': tipo
    }
    return render(request, 'messages.html', context)

@login_required(login_url='/login/')
def delete_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    inmueble.delete()
    return HttpResponseRedirect('/inmuebles/')

@login_required(login_url='/login/')
def modal_inmueble(request, pk):
    usuario = request.user
    tipo = get_object_or_404(Perfil, usuario=usuario).tipo_usuario.tipo
    inmueble = get_object_or_404(Inmueble, pk=pk)
    
    context = {
        'inmueble': inmueble,
        'tipo': tipo,
        'title': 'Detalles del Inmueble'
    }
    return render(request, 'modal.html', context)

def prueba(request):
    return render(request, 'prueba.html')
