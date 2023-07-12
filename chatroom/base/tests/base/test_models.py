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
    

import pytest

pytestmark = pytest.mark.django_db

class TestTopicMaodel:
    def test_str_return(self, topic_factory):
        topic = topic_factory(name="test-topic-name")
        assert topic.__str__() == "test-topic-name"


class TestRoomMaodel:
    def test_str_return(self, room_factory):
        room = room_factory(name="test-room-name")
        assert room.__str__() == "test-room-name"

