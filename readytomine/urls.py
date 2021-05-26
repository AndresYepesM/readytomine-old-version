from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [

	# Django administration urls
    path('admin/', admin.site.urls),


    # Django authentication urls
    path('accounts/', include('django.contrib.auth.urls')),


    # Users administration site
    re_path('', include('user.urls')),
]
