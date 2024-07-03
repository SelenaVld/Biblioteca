from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Importa la clase User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro
from .forms import LibroForm, CustomUserCreationForm, ProfileImageForm, UserSettingsForm  # Asegúrate de importar UserSettingsForm
import random

def inicio(request):
    libros = list(Libro.objects.all())
    if len(libros) > 3:
        libros = random.sample(libros, 3)
    context = {
        'libros_recomendados': libros
    }
    return render(request, "paginas/inicio.html", context)

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {"libros": libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("libros")
    return render(request, "libros/crear.html", {"formulario": formulario})

def editar(request, id):
    libro = get_object_or_404(Libro, id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect("libros") 
    return render(request, "libros/editar.html", {"formulario": formulario, "libro": libro})

def eliminar(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect("libros")

def buscar_libro(request):
    query = request.GET.get('q')
    if query:
        resultados = Libro.objects.filter(titulo__icontains=query)
    else:
        resultados = Libro.objects.all()
    return render(request, 'libros/buscar.html', {'resultados': resultados, 'query': query})

def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, 'libros/detalle.html', {'libro': libro})

@login_required
def añadir_a_favoritos(request, id):
    libro = get_object_or_404(Libro, id=id)
    if libro in request.user.profile.favoritos.all():
        request.user.profile.favoritos.remove(libro)
    else:
        request.user.profile.favoritos.add(libro)
    return redirect('detalle_libro', id=id)

@login_required
def ver_favoritos(request):
    favoritos = request.user.profile.favoritos.all()
    return render(request, 'libros/favoritos.html', {'favoritos': favoritos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # Limpiar mensajes antes de agregar uno nuevo
        storage = messages.get_messages(request)
        storage.used = True
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuario o contraseña incorrectos')
            else:
                messages.error(request, 'Correo no registrado')
    return render(request, "usuarios/login.html")

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Por favor, inicia sesión.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "usuarios/register.html", {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile = request.user.profile
        if 'imagen' in request.FILES:
            profile.imagen = request.FILES['imagen']
            profile.save()
        return redirect('profile')
    return render(request, 'usuarios/profile.html')

@login_required
def settings_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuración actualizada correctamente.')
            return redirect('profile')
    else:
        form = UserSettingsForm(instance=user)
    return render(request, 'usuarios/settings.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')
