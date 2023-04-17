# turn python object into json
from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField

from base.models import Room


class RoomSerializer(ModelSerializer):
    
    class Meta:
        model = Room
        host = ReadOnlyField(source='host.username')
        # fields = '__all__'
        fields = ['id', 'name', 'topic', 'description', 'host']
        # extra_kwargs = {'host': {'required': True}}