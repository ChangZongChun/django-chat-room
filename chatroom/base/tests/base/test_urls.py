# from django.test import TestCase
# from django.urls import reverse, resolve
# from base.views import home, inRoom, userProfile, createRoom, updateRoom, deleteRoom, deleteMessage, updateUser

# class TestUrls(TestCase):

#     def test_home_url_resolves(self):
#         url = reverse('home')
#         # print(resolve(url))
#         self.assertEqual(resolve(url).func, home)

#     def test_get_home_page(self):
#         # get url localhost:8000/
#         response = self.client.get('')

#         # check which template is used
#         self.assertTemplateUsed(response, 'base/home.html')
#         self.check_templates(self, response)

#         # check response status is equal to 200
#         self.assertEqual(response.status_code, 200)

#     def check_templates(self, response):
#         self.assertTemplateUsed(response, 'main.html')
#         self.assertTemplateUsed(response, 'navbar.html')
#         self.assertTemplateUsed(response, 'base/topic_component.html')
#         self.assertTemplateUsed(response, 'base/feed_component.html')
#         self.assertTemplateUsed(response, 'base/activity_component.html')

#     def test_room_url_resolves(self):
#         url = reverse('room', args=['0000'])
#         # print(resolve(url).func)
#         self.assertEqual(resolve(url).func, inRoom)

#     def test_create_room_url_resolves(self):
#         url = reverse('create-room')
#         # print(resolve(url))
#         self.assertEqual(resolve(url).func, createRoom)

