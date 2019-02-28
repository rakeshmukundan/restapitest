from pytest_testconfig import config


from helper import (call_api_endpoint,
                     validate_response_json,
                     post_form_data)

petIDtotest  = config['petstore']['petIDtoGet']


def test_post_update():
    ''' Send valid post request to update an entry

    '''

    data = {
              "name":"NEw Name",
              "status":'sold'
            }

    resp = post_form_data('/pet/%s'%petIDtotest,data)
    assert resp.status_code == 200
