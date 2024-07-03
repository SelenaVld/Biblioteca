from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("libros/", views.libros, name="libros"),
    path("libros/crear/", views.crear, name="crear_libro"),
    path("libros/editar/<int:id>/", views.editar, name="editar_libro"),
    path("libros/eliminar/<int:id>/", views.eliminar, name="eliminar_libro"),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
    path('libro/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('favoritos/', views.ver_favoritos, name='favoritos'),
    path('añadir-a-favoritos/<int:id>/', views.añadir_a_favoritos, name='añadir_a_favoritos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
