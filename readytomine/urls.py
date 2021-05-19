from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),



    # Home and users home
    path('', views.home, name='home'),

    path('home/', views.admin_home, name='admin_home')
]
