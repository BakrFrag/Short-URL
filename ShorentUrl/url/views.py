from itsdangerous import Serializer
from rest_framework import mixins , viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
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
        print("args:",args,"kwargs:",kwargs);
        code = kwargs.get('shorten_url')
        original_url=get_object_or_404(Shorten,shorten_url=code);
        return HttpResponseRedirect(original_url.original_url);
