Feature: All POST request Test cases
  @Smoke @Regression
  Scenario Outline: POST request
        Given the API endpoint <url>
        When I input a json '<path>' file
        And I perform a POST request
        Then the response code should be <status_code>

        Examples:
        |url                           | path                                    |status_code |
        |/api/users                | ./json_data/user_data.json  | 201              |

   Scenario Outline: POST request edit data
        Given the API endpoint <url>
        When I input a json '<path>' file
        And I perform a POST request
        And I input jsonpath key <name> and value <value1>
        And I input jsonpath key <job> and value <value2>
        Then the response code should be <status_code>

        Examples:
        |url                           | path                                    | name    | value1   | job  | value2                 | status_code |
        |/api/users                | ./json_data/user_data.json  | name   | HazelYu | job  | automation QA    |201               |

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


