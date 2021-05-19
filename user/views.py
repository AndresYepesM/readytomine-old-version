from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

def home(request):

	return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def admin_home(request):
	return render(request, 'home_user.html')