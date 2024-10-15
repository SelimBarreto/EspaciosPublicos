from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # En lugar de 'get', usamos 'filter'
        usuarios = Usuario.objects.filter(email=email)

        if usuarios.exists():
            user = authenticate(request, username=usuarios[0].nombre, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_espacios')  # Redirige a la lista de espacios públicos
            else:
                return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario no encontrado'})

    return render(request, 'usuarios/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rol = request.POST['rol']

        # Crear el usuario de Django y también el usuario personalizado en la tabla 'usuarios'
        user = User.objects.create_user(username=username, email=email, password=password)
        Usuario.objects.create(nombre=username, email=email, contrasena=password, rol=rol)

        # Iniciar sesión automáticamente al registrar un nuevo usuario
        login(request, user)
        return redirect('lista_espacios')  # Redirige a la lista de espacios públicos después del registro

    return render(request, 'usuarios/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige a la página de inicio después de cerrar sesión
