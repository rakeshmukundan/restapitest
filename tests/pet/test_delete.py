from pytest_testconfig import config

from helper import (call_api_endpoint,
                     validate_response_json)

petIDtotest  = config['petstore']['petIDtoDelete']


def test_delete():
    ''' Send valid delete request and validate response

    '''

    resp = call_api_endpoint('/pet/%s'%petIDtotest,
                                'delete')

    assert resp.status_code == 200

