import connexion
import six

from swagger_server import util
import openstack
from flask import json
from flask import Response

def get_flavor():  # noqa: E501
    """Retrieve List of FlavorID

     # noqa: E501


    :rtype: None
    """
    conn = openstack.connect()
    response = ""
    for flavor in conn.compute.flavors():
       # print(server)
        response += json.dumps(flavor, indent=4)
    print(response)    
    return Response(response, mimetype='application/json')
