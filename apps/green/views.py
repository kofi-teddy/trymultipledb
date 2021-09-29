from django.shortcuts import render
from django.views.generic.edit import CreateView

from . models import Green



class Add(CreateView):
    model = Green
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/green'