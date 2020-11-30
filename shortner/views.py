from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from shortner.models import Shorten
from shortner.utils import prefix, save_object


def index(request):
    if request.method == 'POST':
        shorten = save_object(request)
        #print(shorten)
        return render(request, 'shortner/index.html',
                      context={'shortened': '{}://{}/{}{}'.format(request.scheme, request.get_host(), prefix,
                                                                  shorten.shorten_id)})

    return render(request, 'shortner/index.html')


def amplify(request, short_id):
    shorten = Shorten.objects.get(shorten_id=short_id)
    return redirect(shorten.original_url)