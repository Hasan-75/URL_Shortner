import random
from itertools import permutations

from django.db import IntegrityError

from shortner.models import Shorten

prefix = 's/'
li = ['d', '5', '7', 'h', 'n', 'o', 'y', 'k', '6', '8', '9', '1', 'u', 's', 'c', 'g', 'p', 'q', '4', 'e', 'b', '0', 'l',
      'f', 'i', 'm', 'r', 't', 'x', 'w', 'v', 'a', '2', '3', 'j', 'z']


def get_unique_id():
    return ''.join(random.choices(li, k=8))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def save_object(request, i=7777):
    url = request.POST['url']
    id = get_unique_id()
    i += 1
    ip = get_client_ip(request)
    shorten = Shorten(original_url=url, shorten_id=id, ip=ip)
    while True:
        try:
            shorten.save()
            return shorten
        except IntegrityError as e:
            if "original_url" in str(e):
                shorten = Shorten.objects.get(original_url=shorten.original_url)
            else:
                shorten.shorten_id = get_unique_id()
