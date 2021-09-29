from routers.db_routers import Blue
from django.shortcuts import render
from django.views.generic.edit import CreateView

from . models import Blue



def viewdata(request):
    data = Blue.objects.using('blue_db').all()
    return render(request, 'view.html', {'data': data})



class Add(CreateView):
    model = Blue
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/blue'