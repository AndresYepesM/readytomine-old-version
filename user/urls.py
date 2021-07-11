from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from user import views
from .views import UserListView, UpdateUser, DeleteUser

urlpatterns = [
    # Home and users home

    #inicio
    path('', views.Home, name='home'),

    # Home Loggeado
    path('home/', views.Admin_home, name='admin_home'),

    # Formulario de Registro
    path('registro/', views.signup, name='singup'),

    # mensaje de nuevo ususario
    path('Ususario_creado', views.new_userMsj, name='nuevo_ususario'),

    # Listado de Empleados
    path('listado_empleados/', login_required(UserListView.as_view()), name='Listado_empleados'),

    # Update user
    re_path(r'^Editar_usuario/(?P<pk>\d+)$', login_required(UpdateUser.as_view()), name='Editar_ususario'),

    # mensaje de nuevo ususario
    path('Usuario_editado', views.update_userMsj, name='ususario_editado'),

    # Delete User
    re_path(r'^Borrar_ususario(?P<pk>\d+)$', login_required(DeleteUser.as_view()), name='borrar_ususario'),

    # mensaje de nuevo ususario
    path('Usuario_eliminado', views.delete_userMsj, name='ususario_eliminado'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
