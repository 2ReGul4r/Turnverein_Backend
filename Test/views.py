from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# from django.db.models.functions import Lower | queryset = queryset.annotate(lower_attribute=Lower('attribute'))

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def city(request):
    if request.method == 'GET':
        city_list = City.objects.all()
        city = request.query_params.get('city', None)
        postcode = request.query_params.get('postcode', None)
        if city:
            city_list = city_list.filter(city__icontains=city.lower())  
        if postcode:
            city_list = city_list.filter(postcode=postcode)    
        serializer = CitySerializer(city_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        postcode = request.data.get('postcode')
        if postcode:
            try:
                city = City.objects.get(postcode=postcode)
                city.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except City.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def member(request):
    if request.method == 'GET':
        member_list = Member.objects.all()
        id = request.query_params.get('id', None)
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        birthday = request.query_params.get('birthday', None)
        street = request.query_params.get('street', None)
        house_number = request.query_params.get('house_number', None)
        postcode = request.query_params.get('postcode', None)
        if id:
            member_list = member_list.filter(id=id)
        if first_name:
            member_list = member_list.filter(first_name__icontains=first_name.lower())
        if last_name:
            member_list = member_list.filter(last_name__icontains=last_name.lower())
        if birthday:
            member_list = member_list.filter(birthday=birthday)
        if street:
            member_list = member_list.filter(street__icontains=street.lower())
        if house_number:
            member_list = member_list.filter(house_number=house_number)
        if postcode:
            member_list = member_list.filter(postcode=postcode)
        serializer = MemberSerializer(member_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.data.get('id')
        if id:
            try:
                member = Member.objects.get(id=id)
                member.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Member.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def trainer(request):
    if request.method == 'GET':
        trainer_list = Trainer.objects.all()
        id = request.query_params.get('id', None)
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        birthday = request.query_params.get('birthday', None)
        street = request.query_params.get('street', None)
        house_number = request.query_params.get('house_number', None)
        postcode = request.query_params.get('postcode', None)
        if id:
            trainer_list = trainer_list.filter(id=id)
        if first_name:
            trainer_list = trainer_list.filter(first_name__icontains=first_name.lower())
        if last_name:
            trainer_list = trainer_list.filter(last_name__icontains=last_name.lower())
        if birthday:
            trainer_list = trainer_list.filter(birthday=birthday)
        if street:
            trainer_list = trainer_list.filter(street__icontains=street.lower())
        if house_number:
            trainer_list = trainer_list.filter(house_number=house_number)
        if postcode:
            trainer_list = trainer_list.filter(postcode=postcode)
        serializer = TrainerSerializer(trainer_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.data.get('id')
        if id:
            try:
                trainer = Trainer.objects.get(id=id)
                trainer.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Trainer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def sport(request):
    if request.method == 'GET':
        sport_list = Sport.objects.all()
        id = request.query_params.get('id', None)
        name = request.query_params.get('name', None)
        if id:
            sport_list = sport_list.filter(id=id)
        if name:
            sport_list = sport_list.filter(name__icontains=name.lower())
        serializer = SportSerializer(sport_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.query_params.get('id', None)
        if id:
            try:
                sport = Sport.objects.get(id=id)
                sport.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Sport.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def coaching(request):
    if request.method == 'GET':
        coaching_list = Coaching.objects.all()
        id = request.query_params.get('id', None)
        sport = request.query_params.get('sport', None)
        trainer = request.query_params.get('trainer', None)
        if id:
            coaching_list = coaching_list.filter(id=id)
        if sport:
            coaching_list = coaching_list.filter(sport__icontains=sport.lower())
        if trainer:
            coaching_list = coaching_list.filter(trainer__icontains=trainer.lower())
        serializer = CoachingSerializer(coaching_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CoachingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = CoachingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.query_params.get('id', None)
        if id:
            try:
                coaching = Coaching.objects.get(id=id)
                coaching.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Coaching.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)