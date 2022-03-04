from rest_framework import serializers 
from url.models import Shorten

class ShortUrlSerializer(serializers.ModelSerializer):
    url=serializers.URLField(source='original_url')
    class Meta:
        model=Shorten
        fields=['url','shorten_url']
        read_only_fields=('shorten_url',)