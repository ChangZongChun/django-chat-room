import factory

from base.models import User, Room, Topic, Message

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # django_get_or_create = ('username',)

    password = "test_p4w"
    username = "test_username"
    is_superuser = True
    is_staff = True


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    name = "test_topic_name"


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room
    
    # host = factory.SubFactory(UserFactory)
    # topic = factory.SubFactory(TopicFactory)
    name = "test_room_name"



class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message
    
    user = factory.SubFactory(UserFactory)
    room = factory.SubFactory(RoomFactory)
    body = "test_message"