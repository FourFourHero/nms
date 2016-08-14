import logging

# do imports
#from keyvaluestore import KeyValueStore

def model_encode(obj):
    enc = None
    try:
        enc = obj.__json__()
    except:
        logger.exception('Error encoding')
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")

def model_encode_verbose(obj):
    enc = None
    try:
        enc = obj.__json_verbose__()
    except Exception, e:
        logger.exception('Error encoding verbose')
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")