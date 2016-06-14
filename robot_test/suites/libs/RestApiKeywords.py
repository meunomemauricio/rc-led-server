"""Library with the REST API Keywords."""

import httplib
import requests

from robot.api import logger
from robot.api.deco import keyword

WEB_SERVER_URL='http://127.0.0.1:5000/'
MAIN_API_VERSION = 0.1
ACTION_URI='rcled/api/{0}/action'.format(MAIN_API_VERSION)


class RestApiKeywords(object):
    """Keywords to test the REST API using Requests."""

    @keyword('I try to issue a PUT API command with any kind of JSON info')
    def send_any_put_cmd(self):
        self.any_content = {'key':'value'}
        self.last_req = requests.put(
            '{0}{1}'.format(WEB_SERVER_URL, ACTION_URI),
            json=self.any_content,
        )   

    @keyword('the server responds with a ACCEPT')
    def expect_accept_status(self):
        logger.debug('Status Code: {0}'.format(self.last_req.status_code))
        if self.last_req.status_code != requests.codes.accepted:
            raise RuntimeError('Server did not accept our API Call.')

    @keyword('the same information I have sent is echoed back to me')
    def verify_echoed_value(self):
        logger.debug('Received Content: {0}'.format(self.last_req.json()))
        if self.last_req.json() != self.any_content:
            raise RuntimeError('Received information is not the same as sent')
            

