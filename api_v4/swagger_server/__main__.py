#!/usr/bin/env python3


import connexion
import openstack
from swagger_server import encoder


def main():
    conn = openstack.connect()
    if(conn.compute.find_flavor('Standard') is None):
        flavor_standard = conn.compute.create_flavor(name="Standard", vcpus=1, ram=128, disk=2, is_public = True)
        print("Creazione Flavor Standard Riuscita con Successo!")
    else:
        print("Flavor Standard già esistente!")
    

    if(conn.compute.find_flavor('Large') is None):
        flavor_large = conn.compute.create_flavor(name="Large", vcpus=2, ram=256, disk=10, is_public = True)
        print("Creazione Flavor Large Riuscita con Successo!")
    else:
        print("Flavor Large già esistente!")
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Cloud Operations Management'})
    app.run(port=8080)



if __name__ == '__main__':
    main()
