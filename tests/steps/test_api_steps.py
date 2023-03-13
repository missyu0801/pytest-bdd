from pytest_bdd import given, when, then, parsers, scenarios
scenarios("../feature/")
global_container = None


@given(parsers.parse("the API endpoint {url}"))
def method_url(endpoint, url):
    endpoint.url = endpoint.base_url(url)
    return endpoint.url


@when('I perform a GET request')
def perform_get(endpoint):
    endpoint.requests = endpoint.get_request(endpoint.url)
    return endpoint.requests

@when('I perform DELETE request')
def perform_delete(endpoint):
    endpoint.requests = endpoint.delete_request(endpoint.url)
    return endpoint.requests


@when('I perform a PUT request')
def perform_put(endpoint):
    endpoint.requests = endpoint.put_request(endpoint.url, endpoint.json_request)
    return endpoint.requests


@when('I perform a POST request')
def perform_post(endpoint):
    endpoint.requests = endpoint.post_request(endpoint.url, endpoint.json_request)
    return endpoint.requests

@when(parsers.parse('I perform request chaining with method {method}'))
def perform_chain_request(endpoint, method):
    global global_container
    endpoint.requests = endpoint.request_chaining(method, endpoint.url, global_container, endpoint.json_request)
    return endpoint.requests


@when(parsers.parse("I input a json '{path}' file"))
def input_jsonfile(endpoint, path):
    endpoint.json_request = endpoint.open_jsonData(path)
    return endpoint.json_request


# this should be edited depending on your project json schema
@when(parsers.parse('I input jsonpath key {key} and value {value}'))
def identify_key_in_post_request(endpoint, key, value):
    jsonpath = endpoint.identify_key_in_post(endpoint.json_request, key, value)
    endpoint.requests = endpoint.post_request(endpoint.url, endpoint.json_request)
    return jsonpath


@when(parsers.parse('I change input of key {key} and value {value}'))
def identify_key_in_post_request(endpoint, key, value):
    jsonpath = endpoint.identify_key_in_post(endpoint.json_request, key, value)
    return jsonpath


@when(parsers.parse('I stored the value from keyword {key} to {container}'))
def save_value_of_request(endpoint, key, container):
    my_container = endpoint.save_value_from_keyword(endpoint.requests, key, container)
    global global_container
    global_container = my_container
    return my_container


@when(parsers.parse('I stored the request keyword {key} and value {value} to {container}'))
def save_data(endpoint, key, value, container):
    my_container = endpoint.save_request_data(endpoint.requests, key, value, container)
    global global_container
    global_container = my_container
    return my_container


@then(parsers.parse("the response code should be {status_code}"))
def check_response_code(endpoint, status_code):
    endpoint.assert_status_code(endpoint.requests, status_code)


@then(parsers.parse("Verify response content {key} should be {value}"))
def check_json_content(endpoint, key, value):
    value = int(value) if value.isdigit() else value
    endpoint.assert_json_content(endpoint.requests, key, value)


@then(parsers.parse("Verify container key {key} has value {container}"))
def verify_container_value(endpoint, key, container):
    global global_container
    endpoint.assert_save_value_content(endpoint.requests, key, global_container)


@then(parsers.parse("Verify response message should be '{message}'"))
def verify_response_message(endpoint, message):
    endpoint.assert_error_message(endpoint.requests,message)







