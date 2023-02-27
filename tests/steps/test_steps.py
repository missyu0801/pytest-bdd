from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from utilities.base_code import Common
scenarios("../feature/api.feature")

global_url = ""
global_requests = None
global_json_request = None


@pytest.fixture
def endpoint():
    base = Common()
    return base

@given(parsers.parse("the API endpoint {url}"))
def method_url(endpoint,url):
    theurl = endpoint.base_url(url)
    global global_url
    global_url =  theurl
    print(theurl)


@when('I perform a GET request')
def perform_get(endpoint):
    global global_url
    request = endpoint.get_request(global_url)
    global global_requests
    global_requests = request
    print(request.content)
    return request

@when('I perform DELETE request')
def perform_get(endpoint):
    global global_url
    request = endpoint.delete_request(global_url)
    global global_requests
    global_requests = request
    print(request.content)
    return request


@when(parsers.parse("I input a json '{path}' file"))
def input_jsonfile(endpoint, path):
   json_request = endpoint.open_jsonData(path)
   global global_json_request
   global_json_request = json_request
   return  json_request


@when('I perform a POST request')
def perform_post(endpoint):
    global global_url
    global global_json_request
    request = endpoint.post_request(global_url, global_json_request)
    global global_requests
    global_requests = request
    print(request.content)
    return request

@when('I perform a PUT request')
def perform_put(endpoint):
    global global_url
    global global_json_request
    request = endpoint.put_request(global_url, global_json_request)
    global global_requests
    global_requests = request
    print(request.content)
    return request

#this should be edited depending on your project json schema
@when(parsers.parse('I input jsonpath key {key} and value {value}'))
def identify_key_in_post_request(endpoint, key, value):
    global global_url
    global global_json_request
    jsonpath = endpoint.identify_key_in_post(global_json_request,key, value)
    request = endpoint.post_request(global_url, global_json_request)
    global global_requests
    global_requests = request
    print(request.content)
    return jsonpath

@when(parsers.parse('I change input of key {key} and value {value}'))
def identify_key_in_post_request(endpoint, key, value):
    global global_url
    global global_json_request
    jsonpath = endpoint.identify_key_in_post(global_json_request,key, value)
    return jsonpath


@then(parsers.parse("the response code should be {status_code}"))
def check_response_code(endpoint, status_code):
    global global_requests
    endpoint.assert_status_code(global_requests, status_code)
    print(global_requests.status_code)


@then(parsers.parse("Verify response message should be {value}"))
def check_response_message(endpoint,  value):
    global global_requests
    endpoint.assert_json_content(global_requests,  value)
    print(global_requests.json()['message'])

@then(parsers.parse("Verify response content {content} should be {value}"))
def check_json_content(endpoint, content, value):
    global global_requests
    endpoint.assert_json_content(global_requests, content, value)


