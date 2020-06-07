# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestListOfNetworksController(BaseTestCase):
    """ListOfNetworksController integration test stubs"""

    def test_get_network(self):
        """Test case for get_network

        Retrieve List of Network Details
        """
        response = self.client.open(
            '//openstack/network',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
