from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# Create your views here.
def list(request):
    print("Listing")
    return HttpResponse('<h1>hola mundo</h1>')

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
