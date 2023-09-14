from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *
from .serializers import *

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
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
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
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
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
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
        username = request.query_params.get('username', None)
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
        if username:
            trainer_list = trainer_list.filter(username__icontains=username.lower())
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
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        id = request.data.get('id')
        username = request.data.get('username')
        if id:
            try:
                trainer = Trainer.objects.get(id=id)
                trainer.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Trainer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
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
def coursedate(request):
    if request.method == 'GET':
        coursedate_list = Coursedate.objects.all()
        id = request.query_params.get('id', None)
        if id:
            coursedate_list = coursedate_list.filter(id=id)
        serializer = CoursedateSerializer(coursedate_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CoursedateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = CoursedateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.query_params.get('id', None)
        if id:
            try:
                coursedate = Coursedate.objects.get(id=id)
                coursedate.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Coursedate.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def course(request):
    if request.method == 'GET':
        course_list = Course.objects.all()
        id = request.query_params.get('id', None)
        sport = request.query_params.get('sport', None)
        trainer = request.query_params.get('trainer', None)
        if id:
            course_list = course_list.filter(id=id)
        if sport:
            course_list = course_list.filter(sport__icontains=sport.lower())
        if trainer:
            course_list = course_list.filter(trainer__icontains=trainer.lower())
        serializer = CourseSerializer(course_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        id = request.query_params.get('id', None)
        if id:
            try:
                course = Course.objects.get(id=id)
                course.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def participant(request):
    if request.method == 'GET':
        participant_list = Participant.objects.all()
        course = request.query_params.get('course', None)
        member = request.query_params.get('member', None)
        if course:
            participant_list = participant_list.filter(id_course=course)
        if member:
            participant_list = participant_list.filter(id_member=member)
        serializer = ParticipantSerializer(participant_list, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        
    elif request.method == 'DELETE':
        id = request.query_params.get('id', None)
        course = request.query_params.get('course', None)
        member = request.query_params.get('member', None)
        if id:
            try:
                participant = Participant.objects.get(id=id)
                participant.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Participant.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        if course and member:
            try:
                course = Course.objects.get(id_member=member, id_course=course)
                course.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
@authentication_classes([TokenAuthentication])
def toggle_staff_status(request):
    id = request.query_params.get('id', None)
    if not id:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        user = Trainer.objects.get(id=id)
    except Trainer.DoesNotExist:
        return Response({'error': 'Benutzer wurde nicht gefunden.'}, status=status.HTTP_404_NOT_FOUND)

    if user.is_staff:
        user.is_staff = False 
        user.save()
        return Response({'message': 'Administratorstatus des Benutzers wurde entfernt.'}, status=status.HTTP_200_OK)
    else:
        user.is_staff = True
        user.save()
        return Response({'message': 'Benutzer wurde zum Administrator ernannt.'}, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def user_login(request):
    if request.method == 'GET':
        username = request.query_params.get('username', None)
        password = request.query_params.get('password', None)
        
        user = authenticate(request, username=username, password=password)
        
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Ungültige Anmeldeinformationen.'}, status=status.HTTP_401_UNAUTHORIZED)
