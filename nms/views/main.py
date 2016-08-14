import logging

from django.core.cache import cache
from django.contrib.admin.views.decorators import staff_member_required
from nms.views.response import *

logger = logging.getLogger(__name__)

def home(request):
    logger.info('bootstrap')
    
    response_dict = success_dict()
    return render_json(request, response_dict)
