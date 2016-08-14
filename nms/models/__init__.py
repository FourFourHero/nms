import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

# do imports
from player import Player
from system import System
from planet import Planet

import nms.apis.models.system as system_api
import nms.apis.models.planet as planet_api

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
    system = kwargs['instance']
    if not system.name:
        system.name = system_api.create_new_name(system.player)
        logger.info('new system name:' + system.name)
    
@receiver(pre_save, sender=Planet)
def set_planet_name(sender, **kwargs):
    planet = kwargs['instance']
    if not planet.name:
        planet.name = planet_api.create_new_name(planet.system)
        logger.info('new planet name:' + planet.name)
        