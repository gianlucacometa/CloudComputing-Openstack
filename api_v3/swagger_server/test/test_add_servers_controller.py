# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.openstack import Openstack  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAddServersController(BaseTestCase):
    """AddServersController integration test stubs"""

    def test_add_servers(self):
        """Test case for add_servers

        Add a new Servers
        """
        body = Openstack()
        response = self.client.open(
            '//openstack/servers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
