Feature: All Put Request test cases
  Scenario Outline: PUT request
        Given the API endpoint <url>
        When I input a json '<path>' file
        And I change input of key <job> and value <value>
        And I perform a PUT request
        Then the response code should be <status_code>

        Examples:
        |url                           | path                                    | job  | value          | status_code |
        |/api/users/2              | ./json_data/user_data.json | job  | developer   | 200              |


   Scenario Outline: Delete request
        Given the API endpoint <url>
        When I perform DELETE request
        Then the response code should be <status_code>

        Examples:
        |url                            | status_code |
        |/api/users/2              | 204             |




