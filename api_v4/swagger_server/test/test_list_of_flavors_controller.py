# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestListOfFlavorsController(BaseTestCase):
    """ListOfFlavorsController integration test stubs"""

    def test_get_flavor(self):
        """Test case for get_flavor

        Retrieve List of Flavor Name
        """
        response = self.client.open(
            '//openstack/flavor',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
