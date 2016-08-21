import logging
from django.db import models
from nms.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class PlanetManager(models.Manager):
    pass

class Planet(BaseModel):
    system = models.ForeignKey('System', null=False)
    name = models.CharField(max_length=256, default='New Planet', null=True)
    roman_number = models.CharField(max_length=16, default='I', null=True)
    neutral_gold = models.BooleanField(default=False, null=False)
    neutral_emeril = models.BooleanField(default=False, null=False)
    neutral_nickel = models.BooleanField(default=False, null=False)
    neutral_aluminium = models.BooleanField(default=False, null=False)    
    neutral_copper = models.BooleanField(default=False, null=False)
    neutral_iridium = models.BooleanField(default=False, null=False)  
    silicate_chrysonite = models.BooleanField(default=False, null=False)
    exotic_calium = models.BooleanField(default=False, null=False)        
    exotic_omegon = models.BooleanField(default=False, null=False)
    exotic_radnox = models.BooleanField(default=False, null=False)
    exotic_murrine = models.BooleanField(default=False, null=False)
    trade_gravitino = models.BooleanField(default=False, null=False)
    trade_albumen = models.BooleanField(default=False, null=False)
    trade_sac_venom = models.BooleanField(default=False, null=False)    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = PlanetManager()

    class Meta:
        db_table = 'nms_planet'
        app_label = 'nms'

    def __unicode__(self):
        return str(self.id) + ':' + self.full_name()
            
    def full_name(self):
        return self.name + ' ' + self.roman_number
        
    def __json__(self):
        json = {}
        json['id'] = self.id
        json['system'] = self.system
        json['name'] = self.name
        json['roman_number'] = self.roman_number
        json['neutral_gold'] = self.neutral_gold
        json['neutral_emeril'] = self.neutral_emeril
        json['neutral_nickel'] = self.neutral_nickel
        json['neutral_aluminium'] = self.neutral_aluminium
        json['neutral_copper'] = self.neutral_copper
        json['neutral_iridium'] = self.neutral_iridium
        json['silicate_chrysonite'] = self.silicate_chrysonite
        json['exotic_calium'] = self.exotic_calium
        json['exotic_omegon'] = self.exotic_omegon
        json['exotic_radnox'] = self.exotic_radnox
        json['exotic_murrine'] = self.exotic_murrine
        json['trade_gravitino'] = self.trade_gravitino
        json['trade_albumen'] = self.trade_albumen
        json['trade_sac_venom'] = self.trade_sac_venom
        json['created'] = str(self.created)
        json['modified'] = str(self.modified)
        return json