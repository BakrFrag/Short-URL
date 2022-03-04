from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from url.models import *

@admin.register(ClientApiKey)
class ClientAPIKeyModelAdmin(APIKeyModelAdmin):
    """
    register custom API Key Model
    """
    pass
@admin.register(Shorten)
class ShortenAdmin(admin.ModelAdmin):
    search_fields = ['original_url','shorten_url']
    readonly_fields = ['shorten_url']

admin.site.register([Client])