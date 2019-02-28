from helper import (call_api_endpoint,
                     validate_response_json)
from pytest_testconfig import config

petIDtotest  = config['petstore']['petIDtoGet']


def test_get():
    ''' Send valid get request and validate response

    '''

    resp = call_api_endpoint('/pet/%s'%petIDtotest,'get')

    assert resp.status_code == 200
    assert True == validate_response_json(resp,'id')