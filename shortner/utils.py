import random

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from shortner.models import Shorten

prefix = ''
li = ['w', 'W', 'N', 'z', 'T', 'i', 'b', 'L', 'F', '4', 'I', 'j', 'q', 'X', 'x', 'G', '5', 'V', 's', 'K', 'm', 'c', '9',
      '3', '6', 'e', 'p', 'S', 'O', 'M', 'u', 'Y', 'E', 'C', 'Q', 'B', 'y', 'k', 'Z', 'R', '8', 'd', 'o', '2', 'J', 'P',
      '0', 'l', '1', 'f', 'g', 'H', 't', 'a', 'A', '7', 'U', 'r', 'v', 'h', 'n', 'D']


def get_unique_id():
    return ''.join(random.choices(li, k=6))


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
    try:
        shorten.clean_fields()
    except ValidationError as e:
        raise e

    while True:
        try:
            shorten.save()
            return shorten
        except IntegrityError as e:
            if "original_url" in str(e):
                shorten = Shorten.objects.get(original_url=shorten.original_url)
            else:
                shorten.shorten_id = get_unique_id()
