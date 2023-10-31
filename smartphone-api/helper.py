import json
from flask import Response

def eval_int(req):
    return None if req == '' else int(req)

def eval_float(req):
    return None if req == '' else float(req)

def eval_bool(req):
    if req == '1': return True
    elif req == '0': return False
    else: return None

def response(data):
    try:
        return Response(response=json.dumps(data), status=200, mimetype='application/json')
    except:
        return Response(response={}, status=404, mimetype='application/json')