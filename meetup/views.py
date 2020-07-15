from django.shortcuts import render
from django.utils import timezone
from .models import Evento

# Create your views here.

def post_list(request):
    eventos = Evento.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'meetup/post_list.html', {'eventos': eventos})

