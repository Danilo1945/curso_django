from django.http import HttpResponse
from django.shortcuts import render

from django.core import serializers
from django.http import JsonResponse
from .models import Move, MoveLine
import json


# from .forms import MoveForm

# Create your views here.


# Create your views here.


def move_list(request):
    moves = Move.objects.all()
    context = {"title": "Lista de Facturas", "moves_ids": moves}

    data_render = render(request, 'move/account_list.html', context)
    return data_render


def move_line_list(request):
    move_lines = MoveLine.objects.all()
    context = {"title": "Lista de  Lineas de Facturas", "moves_line_ids": move_lines}
    data_render = render(request, 'move_line/move_line_list.html', context)
    return data_render

    # return HttpResponse('index')

    # moves = Move.objects.all()
    # data = serializers.serialize('json', moves)
    # return JsonResponse(data, safe=False)

    # moves = Move.objects.all()
    # data = serializers.serialize('json', moves)
    # return JsonResponse(data, safe=False)

    # moves = Move.objects.all()
    # data = serializers.serialize('json', moves)
    # json_data = json.dumps(data, indent=4)
    # return JsonResponse(json_data, safe=False)

    # moves = Move.objects.all().order_by('id')  # all(): Retorna todos los objetos en la tabla "moves".
    # moves = Move.objects.all() # all(): Retorna todos los objetos en la tabla "moves".
    # moves = Move.objects.filter(name="FA 001-002-000000001")
    # name__icontains equivalente al ILIKE
    # moves = Move.objects.filter(name__icontains='0002') # name ilike ilike '%0001%'
    '''__lt para valores menores que un número
       __gte para valores mayores o iguales a un número
       __lte para valores menores o iguales a un número
       __range para valores dentro de un rango, como total__range=(50, 100) para
       '''
    # moves = Move.objects.all()
    # data = serializers.serialize('json', moves)
    # return JsonResponse(data, safe=False)

    # moves = Move.objects.filter(total__gt=100)  # total > 100

    # context = {"title": "Lista de Facturas", "moves_ids": moves}
    # return render(request, 'account/account_list.html', context)
