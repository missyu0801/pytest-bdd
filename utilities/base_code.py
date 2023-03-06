import configparser
import json
import jsonpath
from jsonpath_ng import parse
import requests


class Common:

#--------------------------------------------------------------------------------------------------------------------------------
# Code for API's
#-----------------------------------------------------------------------------------------------------------------------------------

    def base_url(self, url):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        baseurl = config['api']['endpoint']
        theurl = f'{baseurl}{url}'
        return theurl

    #edit this depending on your project's api header
    def api_header(self):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        header = {
            'Content-Type': config['apiheaders']['content_type'],
            'Connection': config['apiheaders']['connection']
            #Authorization: bearer or basis config add in config file
        }
        return header

    def open_jsonData(self, path):
        with open(path) as f:
            json_request = json.loads(f.read())
        return json_request

    def get_request(self, method_url):
        result = requests.get(method_url, headers = self.api_header())
        return result

    def post_request(self, method_url, json_file):
        result = requests.post(method_url, json = json_file, headers = self.api_header())
        return result

    def put_request(self, method_url, json_file):
        result = requests.put(method_url, json = json_file, headers = self.api_header())
        return result

    def delete_request(self, method_url):
        result = requests.delete(method_url, headers = self.api_header())
        return result

    #change this code depending on your json schema reference to jsonpath
    def identify_key_in_post(self, jsonrequest,key, value):
        jsonpath =parse("$."+key)
        jsonpath_expr = jsonpath.update(jsonrequest, value)
        return jsonpath_expr

    def assert_status_code(self, response,statuscode):
        assert response.status_code == int(statuscode)


    def assert_json_content(self,response, key, val):
        json_data = response.json()
        jsonpath_expr = parse("$."+key)
        match = jsonpath_expr.find(json_data)
        expected_val = val
        actual_val = match[0].value if match else None
        print(f"Expected {expected_val}, got {actual_val}")
        assert actual_val == expected_val
#------------------------------------------------------------------------------------------------------------------------------------
# Code for GUI
#------------------------------------------------------------------------------------------------------------------------------------

