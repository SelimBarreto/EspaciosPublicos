from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_espacios, name='lista_espacios'),
    path('<int:id>/', views.detalle_espacio, name='detalle_espacio'),  # Mantén solo esta línea
    path('mapa/', views.mapa_interactivo, name='mapa_interactivo'),
    path('<int:id>/foros/', include('foros.urls')),  # Ruta para los foros dentro del espacio
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
