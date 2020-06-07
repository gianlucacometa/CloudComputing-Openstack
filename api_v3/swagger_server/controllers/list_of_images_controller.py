import connexion
import six


from swagger_server import util
import openstack
from flask import json
from flask import Response


def get_image():  # noqa: E501
    """Retrieve List of ImageID

     # noqa: E501


    :rtype: None
    """
    conn = openstack.connect()
    response = ""
    for image in conn.compute.images():
       # print(server)
        response += json.dumps(image, indent=4)
    print(response)    
    return Response(response, mimetype='application/json')
