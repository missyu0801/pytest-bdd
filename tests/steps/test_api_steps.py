from pytest_bdd import given, when, then, parsers, scenarios

scenarios("../feature/")

@given(parsers.parse("the API endpoint {url}"))
def method_url(endpoint,url):
    theurl = endpoint.base_url(url)
    global global_url
    global_url =  theurl
    print(theurl)
    return theurl

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


@then(parsers.parse("Verify response content {key} should be {value}"))
def check_json_content(endpoint, key, value):
    global global_requests
    value = int(value) if value.isdigit() else value
    endpoint.assert_json_content(global_requests, key, value)


