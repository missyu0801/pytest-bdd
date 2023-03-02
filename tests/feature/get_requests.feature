Feature: All Get request  Test Cases
  @Smoke @Regression
  Scenario Outline: GET request
        Given the API endpoint <url>
        When I perform a GET request
        Then the response code should be <status_code>
        And  Verify response content <data0_email> should be <email0_value>
        And  Verify response content <data0_name> should be <name0_value>


        Examples:
        |url                           | status_code |  data0_email  | email0_value                       | data0_name          | name0_value |
        |/api/users?page=2  | 200               | data[0].email  | michael.lawson@reqres.in | data[0].first_name | Michael          |
        |/api/users/2             | 200                | data.email     |  janet.weaver@reqres.in     | data.first_name    | Janet              |


