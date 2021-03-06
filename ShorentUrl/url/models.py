from uuid import uuid4
from django.db import models
from django.conf import settings
from rest_framework_api_key.models import AbstractAPIKey
# Create your models here.
class Shorten(models.Model):
    """
    model reprsents shorten url attributes 
    """
    original_url = models.URLField(unique=True);
    shorten_url = models.URLField(unique=True);

    def __str__(self):
        """
        
        """
        return self.shorten_url;

    def generate_short_url(self):
        """
        generate shorten url from random alphanumeric 
        """
        short_url=''
        while True:
            random_alpha_char= str(uuid4())[0:8];
            if Shorten.objects.filter(shorten_url=random_alpha_char).exists():
                continue;
            short_url = random_alpha_char;
            break;
        return short_url
    def save(self,*args,**kwargs):
        """
        overide save method to include shorten_url as random string of alpha numeric 
        """
        
        try:
                 obj=Shorten.objects.get(original_url=self.original_url)
                 self.shorten_url=obj.shorten_url
        except:
                 code=self.generate_short_url();
                 self.shorten_url=settings.DEFAULT_URL.format(code)
                 return super().save(*args,**kwargs);

class Client(models.Model):
    """
    reprsents client 
    """
    name=models.CharField(max_length=256,unique=True);


class ClientApiKey(AbstractAPIKey):
    """
    overide default api key
    client 1:N ApiKey
    """
    client=models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="api_keys",
    );
    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Client Api Key"
        verbose_name_plural = "Client Api Keys"