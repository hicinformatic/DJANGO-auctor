from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
    
from .apps import AuctorConfig as conf
from .models import Article
from .auctorcode import AuctorCode

@receiver(pre_save, sender=Article)
def AuctorCoding(sender, instance, **kwargs):
    auccode = AuctorCode(instance.content_ac)
    instance.content = auccode.Encoding()