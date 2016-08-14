import logging
from nms.models import Player

logger = logging.getLogger(__name__)

def create(name):
    player = Player()
    player.name = name
    update(player)
    return player

def update(player):
    player.save()

def delete(player):
    player.delete()
    
def get_by_name(name):
    try:
        return Player.objects.get(name=name)
    except:
        logger.exception('error getting player')
    return None