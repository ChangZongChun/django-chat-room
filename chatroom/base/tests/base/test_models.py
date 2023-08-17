# from django.test import TestCase
# from base.models import User, Room

# class TestRoomMaodel (TestCase):


    # def setUp(self):
    #     self.user = User.objects.create(
    #         name = 'django', email = 'django@email.com')
    #     self.room_test = Room.objects.create(
    #         host = self.user, name = 'test', topic = ''
    #         )
        
    # def test_room_is_created(self):
    
from base.models import User, Topic
import pytest

pytestmark = pytest.mark.django_db

class TestTopicMaodel:
    """ Test Topic Model return topic name """
    def test_str_return(self, topic_factory):
        topic = topic_factory(name="test-topic-name")
        assert topic.__str__() == "test-topic-name"
        print(Topic.objects.all())


class TestRoomMaodel:
    """ Test Room Model return room name """
    def test_str_return(self, room_factory):
        room = room_factory(name="test-room-name")
        assert room.__str__() == "test-room-name"
    

class TestMessageModel:
    """ Test Message Model return message body """
    def test_str_return(self, message_factory):
        message = message_factory(body="test-message-body")
        assert message.__str__() == "test-message-body"
        print(message.user.username)
        assert len(message.__str__()) < 50
