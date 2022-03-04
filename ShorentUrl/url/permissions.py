from rest_framework_api_key.permissions import BaseHasAPIKey
from url.models import ClientApiKey

class HasClientApiKey(BaseHasAPIKey):
    model = ClientApiKey