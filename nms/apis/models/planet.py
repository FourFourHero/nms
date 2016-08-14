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

def get_by_full_name(name):
    try:
        return Planet.objects.get(name=name, roman_number=roman_number)
    except:
        logger.exception('error getting planet')
    return None

def get_by_system(system):
    try:
        return list(Planet.objects.filter(system=system))
    except:
        logger.exception('error getting planet')
    return []

def get_all_by_name(name):
    try:
        return list(Planet.objects.filter(name=name))
    except:
        logger.exception('error getting planets')
    return []

def create_new_name(planet):
    system = planet.system
    count = 0
    while count < 1000:
        name = ''
        
        system_suf = system.name
        system_suf = system_suf.split(' ')
        system_suf = system_suf[0][0] + system_suf[1][0] + system_suf[2][0]
        logging.info(system_suf)
        #name = system_suf
        logger.info(name)
        
        neutral = ''
        if planet.neutral_aluminium:
            neutral += 'al'
        if planet.neutral_copper:
            neutral += 'co'
        if planet.neutral_emeril:
            neutral += 'em'
        if planet.neutral_gold:
            neutral += 'go'
        if planet.neutral_iridium:
            neutral += 'ir'
        if planet.neutral_nickel:
            neutral += 'ni'
            
        if neutral:
            name += ' ' + neutral.capitalize()
        logger.info(name)
        
        exotic = ''
        if planet.exotic_calium:
            exotic += 'cal'
        if planet.exotic_murrine:
            exotic += 'mur'
        if planet.exotic_omegon:
            exotic += 'ome'
        if planet.exotic_radnox:
            exotic += 'rad'
        
        if exotic:
            name += ' ' + exotic.capitalize()
        logger.info(name)
                
        trade = ''
        if planet.trade_albumen:
            trade += 'albu'
        if planet.trade_gravitino:
            trade += 'grav'

        if trade:
            name += ' ' + trade.capitalize()
        logger.info(name)

        planets = get_all_by_name(name)
        num_planets = len(planets)
        
        roman_number = roman_api.toRoman(num_planets + 1)
        logger.info(name + ' ' + roman_number)
        
        logger.info('checking planet name: ' + name + ' ' + roman_number)
        planet = get_by_full_name(name, roman_number)
        if not planet:
            return name, roman_number
        count += 1
        
    raise Exception('tried 1000 times to get a new name and failed')