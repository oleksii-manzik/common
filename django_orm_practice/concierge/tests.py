from django.test import TestCase

from concierge.models import Key, Apartment


class KeyModelTests(TestCase):

    def test_key_model_creation_positive_case(self):
        apartment = Apartment(number=2)
        apartment.save()
        key = Key(apartment=apartment)
        key.save()
        keys = Key.objects.all()
        self.assertEquals(keys[0].apartment.number, 2)
        self.assertEquals(keys[0].id, 1)
