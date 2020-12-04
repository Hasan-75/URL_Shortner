from rest_framework import serializers
from shortner.models import Shorten
from shortner.utils import prefix


class ShortenSerializer(serializers.HyperlinkedModelSerializer):
    shorten_url = serializers.SerializerMethodField()

    class Meta:
        model = Shorten
        fields = ['id', 'original_url', 'shorten_url', 'shorten_id']

    def get_shorten_url(self, instance):
        request = self.context.get('request')
        return '{}://{}/{}{}'.format(request.scheme, request.get_host(), prefix,
                                     instance.shorten_id)
