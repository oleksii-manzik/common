from http import HTTPStatus
import requests

from django.test import TestCase
from django.test import Client

from django.urls import reverse


class HealthCheckTests(TestCase):
    client = Client()

    def test_health_check(self):
        response = self.client.get(reverse('health_check'))

        with self.subTest('status code'):
            self.assertEqual(response.status_code, HTTPStatus.OK)

        with self.subTest('response'):
            self.assertEqual(response.content, b'ok')


class ChuckNorrisApiTests(TestCase):
    client = Client()

    def test_view_status_code(self):
        response = self.client.get(reverse('get_joke'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_api_joke_presence(self):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        self.assertIn('value', response.json())

    def test_api_wrong_joke_id(self):
        response = requests.get('https://api.chucknorris.io/jokes/ololo')

        with self.subTest('status code'):
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

        with self.subTest('response'):
            self.assertEqual(response.json().get('message'),
                             'Joke with id "ololo" not found.')
