from django.shortcuts import render
from .models import Technik, Territory, OrderDuration, Order

# Create your views here.

def index(request):
    num_technik=Technik.objects.all().count()
    num_Territory=Territory.objects.all().count()
    num_orderduration=OrderDuration.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_technik':num_technik, 'num_Territory':num_Territory, 'num_orderduration':num_orderduration},
    )