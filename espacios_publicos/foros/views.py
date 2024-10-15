from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Q
from .models import Foro, Comentario
from espacios.models import InstalacionDeportiva
from django.http import JsonResponse


# Función para determinar si un usuario es moderador
def es_moderador(user):
    return user.groups.filter(name='Moderadores').exists()

# Vista para listar foros con funcionalidad de búsqueda
def lista_foros(request, espacio_id):
    espacio = get_object_or_404(InstalacionDeportiva, id=espacio_id)

    query = request.GET.get('q')
    if query:
        foros = Foro.objects.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query),
            espacio=espacio
        )
    else:
        foros = Foro.objects.filter(espacio=espacio)

    return render(request, 'foros/lista_foros.html', {'foros': foros, 'espacio': espacio})

# Vista para mostrar detalles del foro, incluidos los comentarios
def detalle_foro(request, espacio_id, foro_id):
    espacio = get_object_or_404(InstalacionDeportiva, id=espacio_id)
    foro = get_object_or_404(Foro, id=foro_id)
    comentarios = foro.comentarios.all()
    return render(request, 'foros/detalle_foro.html', {'foro': foro, 'espacio': espacio, 'comentarios': comentarios})


# Vista para crear un foro
def crear_foro(request, espacio_id):
    espacio = get_object_or_404(InstalacionDeportiva, id=espacio_id)
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        Foro.objects.create(titulo=titulo, descripcion=descripcion, espacio=espacio, creador=request.user)
        return redirect('lista_foros', espacio_id=espacio_id)
    return render(request, 'foros/crear_foro.html', {'espacio': espacio})



# Vista para eliminar un comentario (solo moderadores)
@user_passes_test(es_moderador)
def eliminar_comentario(request, foro_id, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.delete()
    return redirect('detalle_foro', foro_id=foro_id)

# Vista para editar un comentario (solo moderadores)
@user_passes_test(es_moderador)
def editar_comentario(request, foro_id, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        comentario.contenido = request.POST['contenido']
        comentario.save()
        return redirect('detalle_foro', foro_id=foro_id)
    return render(request, 'foros/editar_comentario.html', {'comentario': comentario})

# Vista para responder a un comentario
def responder_comentario(request, foro_id, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        contenido = request.POST['contenido']
        Comentario.objects.create(foro=comentario.foro, usuario=request.user, contenido=contenido, respuesta_a=comentario)
    return redirect('detalle_foro', foro_id=foro_id)

# Vista para dar "like" a un comentario
def like_comentario(request, foro_id, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.likes += 1
    comentario.save()
    return redirect('detalle_foro', foro_id=foro_id)


@login_required
def agregar_comentario(request, espacio_id, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            comentario = Comentario.objects.create(
                foro=foro,
                usuario=request.user,
                contenido=contenido
            )
            comentario.save()

            # Si la solicitud es AJAX, devolvemos una respuesta JSON con los datos del comentario
            if request.is_ajax():
                return JsonResponse({
                    'status': 'ok',
                    'contenido': comentario.contenido,
                    'usuario': comentario.usuario.username,
                    'fecha': comentario.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
                })

            # Si no es AJAX, redirigimos normalmente
            return redirect('detalle_foro', espacio_id=espacio_id, foro_id=foro.id)

    return redirect('detalle_foro', espacio_id=espacio_id, foro_id=foro.id)