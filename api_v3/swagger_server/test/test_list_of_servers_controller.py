# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestListOfServersController(BaseTestCase):
    """ListOfServersController integration test stubs"""

    def test_get_server(self):
        """Test case for get_server

        Retrieve Complete List of Servers
        """
        response = self.client.open(
            '//openstack/servers',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
