import logging

from nms.models import Planet
import nms.apis.color as color_api
import nms.apis.feeling as feeling_api
import nms.apis.animal as animal_api
import nms.apis.roman as roman_api

logger = logging.getLogger(__name__)

def create(system, name):
    planet = Planet()
    planet.system = system
    planet.name = name
    logger.info('creating planet: ' + planet.name)
    update(planet)
    return planet

def update(planet):
    planet.save()

def delete(planet):
    planet.delete()
    
def get_by_name(name):
    try:
        return Planet.objects.get(name=name)
    except:
        logger.exception('error getting planet')
    return None

def get_by_system(system):
    try:
        return list(Planet.objects.filter(system=system))
    except:
        logger.exception('error getting planet')
    return None

def create_new_name(system):
    count = 0
    while count < 1000:
        name = ''
        
        system_suf = system.name
        system_suf = system_suf.split(' ')
        system_suf = system_suf[0][0] + system_suf[1][0] + system_suf[2][0]
        
        name = system_suf
        logger.info(name)
        
        neutral = ''
        if planet.resource_aluminium:
            neutral += 'al'
        if planet.resource_copper:
            neutral += 'co'
        if planet.resource_emeril:
            neutral += 'em'
        if planet.resource_gold:
            neutral += 'go'
        if planet.resource_iridium:
            neutral += 'ir'
        if planet.resource_nickel:
            neutral += 'ni'
            
        if neutral:
            name = ' ' + neutral.capitalize()
        logger.info(name)        
        
        exotic = ''
        if planet.exotic_calium:
            exotic += 'ca'
        if planet.exotic_murrine:
            exotic += 'mu'
        if planet.exotic_omegon:
            exotic += 'om'
        if planet.exotic_radnox:
            exotic += 'ra'
        
        if exotic:
            name += ' ' + exotic.capitalize()
        logger.info(name)
                
        trade = ''
        if planet.trade_albumen:
            trade += 'alb'
        if planet.trade_gravitino:
            trade += 'grav'

        if trade:
            name += ' ' + trade.capitalize()
        logger.info(name)   
        
        pis = get_by_system(system)
        np = len(pis)
        
        roman_num = roman_api.toRoman(np + 1)
        name += ' ' + roman_num
        logger.info(name)
        
        logger.info('checking planet name: ' + name)
        planet = get_by_name(name)
        if not planet:
            return name
        count += 1
        
    raise Exception('tried 1000 times to get a new name and failed')