from django.db import models

class BaseModel(models.Model):

    def __json__(self):
        return None

    def __json_verbose__(self):
        return self.__json__()

    def __json_short__(self):
        return self.__json__()

    def __eq__(self, that):
        if that:
            return self.id == that.id
        return False
        
    class Meta:
        abstract = True