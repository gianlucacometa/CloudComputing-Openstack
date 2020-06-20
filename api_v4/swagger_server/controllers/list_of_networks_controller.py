import connexion
import six
from swagger_server import util
import openstack
from flask import json
from flask import Response


def get_network():  # noqa: E501
    conn = openstack.connect()
    response = []
    for network in conn.network.networks():
        networkObj = json.dumps(network)
        response.append(json.loads(networkObj))
    print(json.dumps(response, indent=4))    
    return Response(json.dumps(response, indent=4), mimetype='application/json')
