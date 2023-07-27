from pytest_factoryboy import register

from .factories import UserFactory, RoomFactory, TopicFactory, MessageFactory

register(UserFactory)
register(TopicFactory)
register(RoomFactory)
register(MessageFactory)