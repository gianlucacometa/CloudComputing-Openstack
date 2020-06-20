import connexion
import six
from swagger_server import util
import openstack
from flask import json
from flask import Response

def get_flavor():  # noqa: E501
    conn = openstack.connect()
    response = []
    for flavor in conn.compute.flavors():
        flavorObj = json.dumps(flavor)
        response.append(json.loads(flavorObj))
    print(json.dumps(response, indent=4))    
    return Response(json.dumps(response, indent=4), mimetype='application/json')
