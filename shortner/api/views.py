from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shortner.api.serializers import ShortenSerializer
from shortner.utils import save_object


@api_view(['POST'])
def api_shorten(request):
    if request.method == 'POST':
        try:
            shorten = save_object(request)
        except ValidationError as e:
            return Response(e.error_dict, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = ShortenSerializer(shorten, context={'request': request})
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
