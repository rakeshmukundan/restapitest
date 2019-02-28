from helper import (call_api_endpoint,
                     validate_response_json)
from pytest_testconfig import config



def test_findbystatus():
    ''' Send findbystatus request and validate response

    '''

    resp = call_api_endpoint('/pet/findByStatus',
                                'get',
                                params={'status':['available']})
    
    assert resp.status_code == 200
