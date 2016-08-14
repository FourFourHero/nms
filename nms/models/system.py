import logging
from django.db import models
from nms.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class SystemManager(models.Manager):
    pass

class System(BaseModel):
    player = models.ForeignKey('Player', null=False)
    name = models.CharField(max_length=256, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = SystemManager()

    class Meta:
        db_table = 'nms_system'
        app_label = 'nms'

    def __unicode__(self):
        return str(self.id) + ':' + self.name
            
    def __json__(self):
        json = {}
        json['id'] = self.id
        json['player'] = self.player
        json['name'] = self.name
        json['created'] = str(self.created)
        json['modified'] = str(self.modified)
        return json