from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

import concierge.models as models
from concierge.forms import KeyTransferForm


def health_check(request):
    return HttpResponse("OK")


def key_transfer_created(request):
    return HttpResponse("Key transfer was created")


def index(request):
    html_text = render_to_string('index.html', {'title': 'concierge'})
    return HttpResponse(html_text)


def api_serializer(request, model_type, object_id):
    try:
        model = getattr(models, model_type.capitalize())
        serializer_name = request.GET['format']
        instance = model.objects.get(id=object_id)
        return HttpResponse(serializers.serialize(serializer_name, [instance]))
    except (AttributeError, SerializerDoesNotExist,
            models.Person.DoesNotExist, models.Apartment.DoesNotExist,
            models.Key.DoesNotExist):
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class KeyTransferView(FormView):
    template_name = 'key_transfer_form.html'
    form_class = KeyTransferForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save_key_transfer()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse('Invalid data')
