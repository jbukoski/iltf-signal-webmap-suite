from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
import json
import os

def index(request):
    return render(request, 'index.html', {
    })

def custLogin(request):

    print("\n\n================")
    print(request.user.username)
    print("==================\n\n")
    
    if request.user.username == 'tamaya_user':
        return HttpResponseRedirect(reverse('tamaya_index'))
    elif request.user.username == 'comanche_user':
        return HttpResponseRedirect(reverse('comanche_index'))
    else:
        return redirect('iltf_index')

