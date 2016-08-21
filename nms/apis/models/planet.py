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

def get_by_full_name(name, roman_number):
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
        
        neutral = []
        if planet.neutral_aluminium:
            neutral.append(alu)
        if planet.neutral_copper:
            neutral.append(cop)
        if planet.neutral_emeril:
            neutral.append(eme)
        if planet.neutral_gold:
            neutral.append(gold)
        if planet.neutral_iridium:
            neutral.append(iri)
        if planet.neutral_nickel:
            neutral.append(ni)
                
        silicate = []
        if planet.silicate_chrysonite:
            silicate.append(chrys)
                
        exotic = []
        if planet.exotic_calium:
            exotic.append(cal)
        if planet.exotic_murrine:
            exotic.append(mur)
        if planet.exotic_omegon:
            exotic.append(omeg)
        if planet.exotic_radnox:
            exotic.append(rad)
                
        trade = []
        if planet.trade_albumen:
            trade.append(albu)
        if planet.trade_gravitino:
            trade.append(grav)
        if planet.trade_sac_venom:
            trade.append(sac)

        words = neutral + silicate + exotic + trade
        num_words = len(words)
        
        if num_words == 0:
            name = system_suf
            name = name.upper()
        elif num_words == 1:
            name = words[0].name
            name = name.capitalize()
        else:
            for word in words:
                name += word.short
            name = name.capitalize()
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

class Resource(object):
    name = None
    short = None

alu = Resource()
alu.name = 'aluminium'
alu.short = 'alu'
cop = Resource()
cop.name = 'copper'
cop.short = 'cop'
eme = Resource()
eme.name = 'emeril'
eme.short = 'bam'
gold = Resource()
gold.name = 'gold'
gold.short = 'go'
iri = Resource()
iri.name = 'iridium'
iri.short = 'irid'
ni = Resource()
ni.name = 'nickel'
ni.short = 'ni'
chrys = Resource()
chrys.name = 'chyrsonite'
chrys.short = 'chrys'
cal = Resource()
cal.name = 'calium'
cal.short = 'cal'
mur = Resource()
mur.name = 'murrine'
mur.short = 'mur'
omeg = Resource()
omeg.name = 'omegon'
omeg.short = 'omeg'
rad = Resource()
rad.name = 'radnox'
rad.short = 'rad'
grav = Resource()
grav.name = 'gravitino'
grav.short = 'grav'
albu = Resource()
albu.name = 'albumen'
albu.short = 'albu'
sac = Resource()
sac.name = 'venom'
sac.short = 'ven'