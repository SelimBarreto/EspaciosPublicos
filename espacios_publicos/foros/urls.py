from django.urls import path
from . import views

urlpatterns = [
    path('<int:espacio_id>/foros/', views.lista_foros, name='lista_foros'),
    path('<int:espacio_id>/foros/crear/', views.crear_foro, name='crear_foro'),
    path('foros/<int:foro_id>/', views.detalle_foro, name='detalle_foro'),
    path('foros/<int:foro_id>/comentarios/<int:comentario_id>/responder/', views.responder_comentario, name='responder_comentario'),
    path('foros/<int:foro_id>/comentarios/<int:comentario_id>/like/', views.like_comentario, name='like_comentario'),
    path('foros/<int:foro_id>/comentarios/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('foros/<int:foro_id>/comentarios/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('foros/<int:foro_id>/comentar/', views.agregar_comentario, name='agregar_comentario'),
    path('espacios/<int:espacio_id>/foros/<int:foro_id>/', views.detalle_foro, name='detalle_foro'),
]


