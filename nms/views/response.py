import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from nms.models import model_encode
from nms.models import model_encode_verbose

###
### Request Handling
###

def get_request_var(request, name):
    var = None
    try:
        var = request.POST[name]
    except:
        try:
            var = request.GET[name]
        except:
            pass
    
    if var == '':
        var = None
    
    return var

###
### Responses
###

def error_dict(http_status_code=400):
    error_dict = _response_dict()
    error_dict['error_code'] = 1
    error_dict['error_msg'] = 'Unknown error'
    error_dict['http_status_code'] = http_status_code
    return error_dict

def success_dict(http_status_code=200):
    success_dict = _response_dict()
    success_dict['error_code'] = 0
    success_dict['error_msg'] = ''
    success_dict['http_status_code'] = http_status_code
    return success_dict

def render_template(request, template, template_values=None, verbose=False, minify=True):
    http_status = 200
    if template_values:
        try:
            http_status = template_values['http_status_code']
        except:
            pass
    return render(request, template, template_values, status=http_status)

def render_json(request, json_values, verbose=False, minify=True):
    http_status = json_values['http_status_code']
    encode = model_encode
    if verbose:
        encode = model_encode_verbose
    
    response_data = json.dumps(json_values, default=encode)
    return HttpResponse(response_data, content_type="application/json", status=http_status)

def render_400(request, template_values=None):
    return render(request, '400.html', template_values, status=400)

def render_500(request, template_values=None):
    return render(request, '500.html', template_values, status=500)

def response_json_500(request, json_values=None):
    json_values = json_values or error_dict(http_status_code=500)
    json_values['error_code'] = 500
    return render_json(request, json_values=json_values)

def response_json_503(request, json_values=None):
    json_values = json_values or error_dict(http_status_code=503)
    json_values['error_code'] = 503
    json_values['error_msg'] = 'Service not available'
    return render_json(request, json_values=json_values)

def redirect_to_url(url):
    return redirect(url)

###
### PRIVATE
###

def _response_dict():
    response_dict = {}
    response_dict['error_code'] = 0
    response_dict['error_msg'] = ''
    response_dict['http_status_code'] = 200
    return response_dict