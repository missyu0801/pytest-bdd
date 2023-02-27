import configparser
import json
import jsonpath
from jsonpath_ng import parse
import requests

class Common:

    def base_url(self, url):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        baseurl = config['api']['endpoint']
        theurl = f'{baseurl}{url}'
        return theurl

    def open_jsonData(self, path):
        with open(path) as f:
            json_request = json.loads(f.read())
        return json_request

    def get_request(self, method_url):
        result = requests.get(method_url)
        return result

    def post_request(self, method_url, json_file):
        result = requests.post(method_url, json = json_file)
        return result

    def put_request(self, method_url, json_file):
        result = requests.put(method_url, json = json_file)
        return result

    def delete_request(self, method_url):
        result = requests.delete(method_url)
        return result

    #change this code depending on your json schema reference to jsonpath
    def identify_key_in_post(self, jsonrequest,key, value):
        jsonpath =parse("$."+key)
        jsonpath_expr = jsonpath.update(jsonrequest, value)
        return jsonpath_expr

    def assert_status_code(self, response,statuscode):
        assert response.status_code == int(statuscode)

    def assert_response_message(self, response, value):
        assert response.json()['message'] == value

    def assert_json_content(self,response, content, value):
        response_result = json.loads(response.text)
        jsonpath.jsonpath(response_result, content) == value



