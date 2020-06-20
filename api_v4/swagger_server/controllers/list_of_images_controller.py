import connexion
import six
from swagger_server import util
import openstack
from flask import json
from flask import Response


def get_image():  # noqa: E501
    conn = openstack.connect()
    response = []
    for image in conn.compute.images():
        imageObj = json.dumps(image)
        response.append(json.loads(imageObj))
    print(json.dumps(response, indent=4))    
    return Response(json.dumps(response, indent=4), mimetype='application/json')
