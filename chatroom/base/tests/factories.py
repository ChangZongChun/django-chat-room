import factory
# from django.contrib.auth.models import User

from base.models import User, Room, Topic

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    name = "test_topic_name"


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room
    
    host = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    name = "test_room_name"
