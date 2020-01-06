import requests
from django.http import HttpResponse
from django.urls import reverse


def health_check(request):
    return HttpResponse('ok')


def link_page(request):
    return HttpResponse(
        f'<a href={reverse(get_joke)}>Get random Chuck Norris joke</a>')


def get_joke(request):
    joke = requests.get('https://api.chucknorris.io/jokes/random').json()
    html = f'<h1>Random Chuck Norris joke</h1><p>{joke.get("value")}</p>'
    return HttpResponse(html)
