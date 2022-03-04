from rest_framework import mixins , viewsets
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from url.models import Shorten
from url.serializers import ShortUrlSerializer
class ShortenUrlViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    include create & get > redirect to url 
    """
    model=Shorten
    lookup_field='shorten_url'
    serializer_class=ShortUrlSerializer
    def retrieve(self,request,*args,**kwargs):
        """
        overide default retrieve method to return http response redirect 
        """
        code = kwargs.get('shorten_url')
        shorten_url= settings.DEFAULT_URL.format(code)
        original_url=get_object_or_404(Shorten,shorten_url=shorten_url);
        return HttpResponseRedirect(original_url.original_url);
