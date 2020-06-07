import connexion
import six

from swagger_server import util
import openstack

from flask import json
from flask import Response


def get_network():  # noqa: E501
    """Retrieve Complete List of Servers
     # noqa: E501
    :rtype: None"""
    response = ""
    conn = openstack.connect()
    for network in conn.network.networks():
       # print(server)
        response += json.dumps(network, indent=4)
    print(response)    
    return Response(response, mimetype='application/json')
