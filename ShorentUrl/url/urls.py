from django.urls import path, include 
from rest_framework import routers
from url.views import ShortenUrlViewSet
router= routers.DefaultRouter();
router.register("v1",ShortenUrlViewSet,basename="v1")
urlpatterns = [
    path('short/',include(router.urls))
]
