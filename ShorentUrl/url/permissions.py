from rest_framework_api_key.permissions import BaseHasAPIKey
from url.models import ClientApiKey

class HasClientApiKey(BaseHasAPIKey):
    """
    overide default api-key model
    allow api key auithentication from custom model ClientApiKey 
    """
    model = ClientApiKey