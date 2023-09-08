from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# from django.db.models.functions import Lower | queryset = queryset.annotate(lower_attribute=Lower('attribute'))

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def stadt(request):
    if request.method == 'GET':
        stadt_list = Stadt.objects.all()
        name = request.query_params.get('name', None)
        if name:
            stadt_list = stadt_list.filter(ort__icontains=name.lower())      
        serializer = StadtSerializer(stadt_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StadtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = StadtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        stadt_plz = request.data.get('plz')
        if stadt_plz:
            try:
                stadt = Stadt.objects.get(plz=stadt_plz)
                stadt.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Stadt.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
