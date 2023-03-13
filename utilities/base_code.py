import configparser
import json
from jsonpath_ng import parse
import requests
import logging
LOGGER = logging.getLogger(__name__)

class Common:
    def __init__(self):
        # the following variables acts as global variables and values  are currently empty
        self.url = None
        self.requests = None
        self.json_request = None


# ------------------------------------------------------------------------------------------------------------------------------------
# Code for API's
# ------------------------------------------------------------------------------------------------------------------------------------

    def base_url(self, url):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        baseurl = config['api']['endpoint']
        theurl = f'{baseurl}{url}'
        LOGGER.info("the base url is: %s", theurl)
        return theurl

    # edit this depending on your project's api header
    def api_header(self):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        header = {
         # 'Content-Type': config['apiheaders']['content_type'],
         'Connection': config['apiheaders']['connection']
         # Authorization: bearer or basis config add in config file
        }
        LOGGER.info(header)
        return header

    def open_jsonData(self, path):
        with open(path) as f:
            json_request = json.loads(f.read())
        LOGGER.info('The json content contains the following data: %s', json_request )
        return json_request

    def get_request(self, method_url):
        result = requests.get(method_url, headers = self.api_header())
        LOGGER.info('The url is: %s, and the request content is: %s', result.url, result.content)
        return result

    def request_chaining(self, method, method_url,storage, json_file=None):
        myurl = method_url+"/"+f"{storage}"
        if method.upper() == "GET":
            result = requests.get(myurl, headers=self.api_header())
        elif method.upper() == "DELETE":
            result = requests.delete(myurl, headers=self.api_header())
        elif method.upper() == "PUT":
            result = requests.put(myurl, json=json_file, headers=self.api_header())
        elif method.upper() == "POST":
            result = requests.post(myurl, json=json_file, headers=self.api_header())
        else:
            raise ValueError(f'Unsupported HTTP method: {method}')
        LOGGER.info('The url is: %s, and the request content is: %s', result.url, result.content)
        return result

    def post_request(self, method_url, json_file):
        result = requests.post(method_url, json = json_file, headers = self.api_header())
        LOGGER.info('The url is: %s, and the request content is: %s', result.url, result.content)
        return result

    def put_request(self, method_url, json_file):
        result = requests.put(method_url, json = json_file, headers = self.api_header())
        LOGGER.info('The url is: %s, and the request content is: %s', result.url, result.content)
        return result

    def delete_request(self, method_url):
        result = requests.delete(method_url, headers = self.api_header())
        LOGGER.info('The url is: %s, and the request content is: %s', result.url, result.content)
        return result

    # change this code depending on your json schema reference to jsonpath
    def identify_key_in_post(self, jsonrequest,key, value):
        jsonpath =parse("$."+key)
        jsonpath_expr = jsonpath.update(jsonrequest, value)
        LOGGER.info('The key is: %s, and the value is: %s', jsonpath, value)
        return jsonpath_expr

    def save_request_data(self, jsonrequest,key, value, container):
        jsonpath =parse("$."+key)
        jsonpath_expr = jsonpath.update(jsonrequest, value)
        container = value
        LOGGER.info('The container value is %s' , container)
        return value

    def save_value_from_keyword(self, response, key, container):
        json_data = response.json()
        saved_value = json_data.get(key)
        if isinstance(container, list):
            container.append(saved_value)
        elif isinstance(container, int) or isinstance(container, str):
            if saved_value is not None:
                container = saved_value
        LOGGER.info('The saved value is: %s', saved_value)
        return saved_value

    def assert_status_code(self, response,statuscode):
        stat_code = response.status_code
        assert stat_code == int(statuscode)
        LOGGER.info('The status code is: %s', stat_code)

    def assert_json_content(self,response, key, val):
        json_data = response.json()
        jsonpath_expr = parse("$."+key)
        match = jsonpath_expr.find(json_data)
        expected_val = val
        actual_val = match[0].value if match else None
        LOGGER.info('The expected value is: %s, and got the value of: %s', expected_val, actual_val)
        assert actual_val == expected_val

    def assert_save_value_content(self, response, key, container):
        saved_value = self.save_value_from_keyword(response, key, container)
        assert saved_value == container, f"Expected value: {container}, Actual value: {saved_value}"
        LOGGER.info('The value contains data: %s', saved_value)
        return saved_value

    def assert_error_message(self, response, my_message):
        response_json = response.json()
        assert response_json["message"] == my_message
        LOGGER.info('Expected message: %s', my_message)
        LOGGER.info('Actual message: %s', response_json["message"])
# -----------------------------------------------------------------------------------------------------------------------------------
# Code for GUI
# ------------------------------------------------------------------------------------------------------------------------------------

