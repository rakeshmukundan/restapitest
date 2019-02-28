from pytest_testconfig import config
import requests
import logging

LOGGER = logging.getLogger(__name__)

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


baseurl = config['petstore']['baseurl']
apikey  = config['petstore']['apikey']

headers = {
    'Content-Type': 'application/json',
    "api_key": apikey
}

headers_form = {
    "api_key": apikey
}

def call_api_endpoint(endpoint,method,**kwargs):
    """ 
    Helper function to call given python request endpoint
    
    Parameters: 
    endpoint: endpoint to which request endpoint call is needed
    method:request method to be called
    args: positional arguements to pass
    kwargs:kwargs to pass
  
    Returns: 
    request response 
  
    """
    url = '%s%s'%(baseurl,endpoint)

    method_to_call = getattr(requests,
                                method)
    resp = method_to_call(url,
                            headers=headers,
                            **kwargs)
    return resp

def post_form_data(endpoint,data):
    """ 
    Helper function to post form data using python request
    
    Parameters: 
    endpoint: endpoint to which request endpoint call is needed
    data: form data to post
  
    Returns: 
    request response 
  
    """
    url = '%s%s'%(baseurl,endpoint)
    resp = requests.post(url,
                            data=data,
                            headers=headers_form)
    return resp

def post_files_data(endpoint,files):
    """ 
    Helper function to upload files using python request
    
    Parameters: 
    endpoint: endpoint to which request endpoint call is needed
    files: filedata to upload
  
    Returns: 
    request response 
  
    """
    url = '%s%s'%(baseurl,endpoint)
    resp = requests.post(url,
                            files=files,
                            headers=headers_form)
    return resp

def validate_response_json(response,element=None):
    """ 
    Helper function to validate if the response has a valid JSON scheme.

    Optionally check the presense of the given element in JSON
  
  
    Parameters: 
    response: python request response object to validate
    element: if passed, check for the presence of this element in JSON

  
    Returns: 
    returns True or False
  
    """
    try:
        data = response.json()
    except:
        LOGGER.exception('Invalid JSON')
        return False
    if element and not data.get(element):
        LOGGER.error('Element %s is not present in JSON'%element)
        return False
    return True