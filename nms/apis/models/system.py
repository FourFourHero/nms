import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from nms.models import System
import nms.apis.color as color_api
import nms.apis.feeling as feeling_api
import nms.apis.animal as animal_api

logger = logging.getLogger(__name__)

def create(player, name):
    system = System()
    system.player = player
    system.name = name
    logger.info('creating system: ' + system.name)
    update(system)
    return system

def update(system):
    system.save()

def delete(system):
    system.delete()
    
def get_by_name(name):
    try:
        return System.objects.get(name=name)
    except:
        logger.exception('error getting system')
    return None
    
def create_new_name(player):
    count = 0
    while count < 1000:
        feeling = feeling_api.random()
        color = color_api.random()
        animal = animal_api.random()
        #name = player.name + "'s " + feeling + ' ' + color + ' ' + animal
        name = feeling + ' ' + color + ' ' + animal
        logger.info('checking system name: ' + name)
        system = get_by_name(name)
        if not system:
            return name
        count += 1
        
    raise Exception('tried 1000 times to get a new name and failed')
    
###
### Pre Save Receiver
###

@receiver(pre_save, sender=System)
def set_system_name(sender, instance, *args, **kwargs):
    system = instance
    system.name = create_new_name(system.player)
    logger.info('receiver system name:' + system.name)
