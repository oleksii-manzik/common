from django import forms

from concierge.models import Key, Person, KeyTransfer


class KeyTransferForm(forms.Form):
    person_name = forms.CharField()
    key_id = forms.NumberInput()

    def save_key_transfer(self):
        key = Key.objects.get(id=int(self.data['key_id']))
        person = Person.objects.get(name=self.data['person_name'])
        transfer_object = KeyTransfer(key_id=key, person_id=person)
        transfer_object.save()
