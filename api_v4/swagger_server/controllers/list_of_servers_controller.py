import connexion
import six
from swagger_server import util
import openstack
from flask import json
from flask import Response


def get_server():  # noqa: E501
    conn = openstack.connect()
    response = []
    for server in conn.compute.servers():
        serverObj = json.dumps(server)
        response.append(json.loads(serverObj))
    print(json.dumps(response, indent=4))    
    return Response(json.dumps(response, indent=4), mimetype='application/json')
