import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

# do imports
from player import Player
from system import System
from planet import Planet

import nms.apis.models.system as system_api

logger = logging.getLogger(__name__)

def model_encode(obj):
    enc = None
    try:
        enc = obj.__json__()
    except:
        logger.exception('Error encoding')
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")

def model_encode_verbose(obj):
    enc = None
    try:
        enc = obj.__json_verbose__()
    except Exception, e:
        logger.exception('Error encoding verbose')
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")
    
###
### Pre Save Receiver
###

@receiver(pre_save, sender=System)
def set_system_name(sender, **kwargs):
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    logger.info('PRE SAVE SYSTEM')
    system = sender
    system.name = system_api.create_new_name(system.player)
    logger.info('receiver system name:' + system.name)
    