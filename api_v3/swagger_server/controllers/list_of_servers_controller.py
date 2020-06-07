import connexion
import six

from swagger_server import util
import openstack

from flask import json
from flask import Response


def get_server():  # noqa: E501
    """Retrieve Complete List of Servers
     # noqa: E501
    :rtype: None"""
    response = ""
    conn = openstack.connect()
    for server in conn.compute.servers():
       # print(server)
        response += json.dumps(server, indent=4)
    print(response)    
    return Response(response, mimetype='application/json')
