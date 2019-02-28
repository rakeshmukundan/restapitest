from pytest_testconfig import config
from six import BytesIO

from helper import (call_api_endpoint,
                     validate_response_json,
                     post_files_data)

petIDtotest  = config['petstore']['petIDtoGet']


def test_img_upload():
    ''' Send valid post request to update an entry

    '''

    files = { "file" :(BytesIO(b'image simulation data'), 'test.jpg') }

    resp = post_files_data('/pet/%s/uploadImage'%petIDtotest,files)
    assert resp.status_code == 200
