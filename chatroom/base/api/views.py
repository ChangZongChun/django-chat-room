import io
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse

from .permissions import IsOwnerOrReadOnly
from base.models import Room, Topic, User
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/create-room'
    ]
    # safe=False allows other languages, except python, in the dictionary 
    return Response(routes)

@api_view(['GET'])
def RoomsList(request):
    rooms = Room.objects.all()
    # many=True serialize multiple objects 
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def getRoom(request, pk):
    

    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return HttpResponse('Room not exists!')

    if request.method == 'GET':
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        topic_name = request.data['topic']
        topic, created = Topic.objects.get_or_create(name=topic_name)

        request.data['topic'] = topic.id

        serializer = RoomSerializer(room, data = request.data)
        if serializer.is_valid():
            serializer.save(host=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        room.delete()
        return Response('room was deleted')

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def createRoom(request):
    topic_name = request.data['topic']
    topic, created = Topic.objects.get_or_create(name=topic_name)

    request.data['topic'] = topic.id
    serializer = RoomSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(host = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)