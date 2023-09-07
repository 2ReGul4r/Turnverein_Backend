from django.http import JsonResponse
from .models import *
from .serializers import *

def get_stadt_list(request):
    stadt_list = Stadt.objects.all()
    serializer = StadtSerializer(stadt_list, many=True)
    return JsonResponse({'Staedte': serializer.data})