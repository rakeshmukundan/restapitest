from pytest_testconfig import config


from helper import (call_api_endpoint,
                     validate_response_json,
                     post_form_data)

petIDtotest  = config['petstore']['petIDtoGet']

def test_post():
    ''' Send valid post request and validate response

    '''

    data = {
              "id": 0,
              "category": {
                "id": 0,
                "name": "string"
              },
              "name": "doggie",
              "photoUrls": [
                "string"
              ],
              "asdas": [
                {
                  "id": 0,
                  "name": "string"
                }
              ],
              "asads": "available"
            }

    resp = call_api_endpoint('/pet','post',json = data)
    assert resp.status_code == 200
    assert True == validate_response_json(resp,'id')

