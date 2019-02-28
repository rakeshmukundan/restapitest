from helper import (call_api_endpoint,
                     validate_response_json)

def test_put():
    ''' Send valid put request and validate response

    '''

    data = {
          "category": {
            "id": 6,
            "name": "name"
          },
          "id": 0,
          "name": "doggie",
          "photoUrls": [
            "photoUrls",
            "photoUrls"
          ],
          "status": "available",
          "tags": [
            {
              "id": 1,
              "name": "name"
            },
            {
              "id": 1,
              "name": "name"
            }
          ]
        }

    resp = call_api_endpoint('/pet','put',json = data)
    assert resp.status_code == 200
    assert True == validate_response_json(resp,'id')


