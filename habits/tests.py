from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(email='test_user@sky.pro',
                                        role='moderator',
                                        phone='0615557766',
                                        city='City'
                                        )

        self.user.set_password('test')
        self.user.save()

        # Создание привычки для тестирования
        self.habit = Habit.objects.create(user=self.user,
                                          place='Moscow',
                                          action='test',
                                          period=2,
                                          lead_time=1)

        # Запрос токена
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'test'})

        self.access_token = response.data.get('access')

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_retrieve_habit(self):
        """Тестирование получения описания привычки"""

        response = self.client.get(
            reverse('habits:get_habit', kwargs={'pk': self.habit.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'place': self.habit.place,
                'time': self.habit.time,
                'action': self.habit.action,
                'is_pleasurable': False,
                'period': self.habit.period,
                'prize': None,
                'lead_time': self.habit.lead_time,
                'public': True,
                'user': self.user.id,
                'associated_habit': None
            }
        )

    def test_list_lesson(self):
        """Тестирование списка спивычек"""

        response = self.client.get(
            reverse('habits:list_habit')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [{
                    'id': self.habit.id,
                    'place': self.habit.place,
                    'time': self.habit.time,
                    'action': self.habit.action,
                    'is_pleasurable': False,
                    'period': self.habit.period,
                    'prize': None,
                    'lead_time': self.habit.lead_time,
                    'public': True,
                    'user': self.user.id,
                    'associated_habit': None
                }]
        )

    def test_update_habit(self):
        """Тестирование изменения привычки"""

        data = {
            'place': 'Beograd',
            'action': 'test_test',
            'period': 1,
            'lead_time': 2
        }

        response = self.client.put(
            reverse('habits:update_habit', kwargs={'pk': self.habit.id}), data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_habit(self):
        """Тестирование создания ривычки"""

        data = {
            'place': 'Beograd',
            'time': '12:12',
            'action': 'test_test',
            'period': 1,
            'lead_time': 2
        }

        response = self.client.post(
            reverse('habits:create_habit'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        response = self.client.delete(
            reverse('habits:delete_habit', kwargs={'pk': self.habit.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(Habit.objects.all().count(), 0)

    def tearDown(self):
        Habit.objects.all().delete()
        User.objects.all().delete()
