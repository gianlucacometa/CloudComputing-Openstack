import connexion
import six

import time
from apscheduler.schedulers.background import BackgroundScheduler

from swagger_server.models.openstack import Openstack  # noqa: E501
from swagger_server import util
import openstack

from flask import json
from flask import Response

def add_servers(body):  # noqa: E501
    """Add a new Servers

     # noqa: E501

    :param body: Employee data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Openstack.from_dict(connexion.request.get_json())  # noqa: E501
        print(body.server_name)
        print(body.image_name)
        
        conn = openstack.connect()
        print(body.image_name+ ", "+  body.flavor_name + ", "+  body.network_name + ", "+ body.server_name)
        
        network = conn.network.find_network(body.network_name)
        image = conn.compute.find_image(body.image_name)
        flavor = conn.compute.find_flavor(body.flavor_name)
        
        creation_time = body.start_creation.split(":")
        destroy_time = body.end_creation.split(":")

        def create():
            server = conn.compute.create_server(
                name=body.server_name, image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}])
            server = conn.compute.wait_for_server(server)

        scheduler = BackgroundScheduler()
        scheduler.add_job(func=create, trigger="cron", hour=creation_time[0], minute=creation_time[1])
        scheduler.start()

        def destroy():
            server = conn.compute.find_server(body.server_name)
            conn.compute.delete_server(server)
        
        scheduler_delete = BackgroundScheduler()
        scheduler_delete.add_job(func=destroy, trigger="cron", hour=destroy_time[0], minute=destroy_time[1])
        scheduler_delete.start()

        result = "Hai schedulato la creazione e distruzione della seguente VM: " + body.server_name + " con Immagine:" +body.image_name + " con Flavor:" + body.flavor_name + " attiva dalle: " + body.start_creation + " alle: " + body.end_creation
        return Response(result, mimetype='text/plain')
    else:
        result = "Assicurati che la richiesta sia di tipo JSON"
        return Response(result, status=400, mimetype='text/plain')
