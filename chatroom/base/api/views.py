from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room, Topic
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    # safe=False allows other languages, except python, in the dictionary 
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # many=True serialize multiple objects 
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'GET':
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # topic_name = request.data['topic']
        # topic, created = Topic.objects.get_or_create(name=topic_name)

        topic_name = request.data['topic']
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.data['name']
        room.description = request.data['description']
        room.topic = topic

        room.save()

        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    
    if request.method =='DELETE':
        room.delete()
        return Response('room was deleted')

@api_view(['POST'])
def createRoom(request):
    # serializer = RoomSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    topic_name = request.data['topic'],
    topic, created = Topic.objects.get_or_create(name=topic_name)
    room = Room.objects.create(
        host = request.user,
        topic = topic,
        name = request.data['name'],
        description = request.data['description']
    )

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)