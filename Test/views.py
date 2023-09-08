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
        plz = request.query_params.get('plz', None)
        if name:
            stadt_list = stadt_list.filter(ort__icontains=name.lower())  
        if plz:
            stadt_list = stadt_list.filter(plz=plz)    
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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def adresse(request):
    if request.method == 'GET':
        adresse_list = Adresse.objects.all()
        id = request.query_params.get('id', None)
        straße = request.query_params.get('straße', None)
        hausnummer = request.query_params.get('hausnummer', None)
        plz = request.query_params.get('plz', None)
        if id:
            adresse_list = adresse_list.filter(id=id)   
        if straße:
            adresse_list = adresse_list.filter(straße__icontains=straße.lower())   
        if hausnummer:
            adresse_list = adresse_list.filter(hausnummer=hausnummer)   
        if plz:
            adresse_list = adresse_list.filter(plz=plz)   
        serializer = AdresseSerializer(adresse_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AdresseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = AdresseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.data.get('id')
        if id:
            try:
                adresse = Adresse.objects.get(id=id)
                adresse.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Adresse.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
