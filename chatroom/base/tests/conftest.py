from pytest_factoryboy import register

from .factories import RoomFactory, TopicFactory

register(TopicFactory)
register(RoomFactory)