Feature: Step arguments
     Scenario Outline: GET request
        Given the API endpoint <url>
        When I perform a GET request
        Then the response code should be <status_code>
        #Then  Verify response content <content> should be <value>

        Examples:
        |url                           | status_code |
        |/api/users?page=2  | 200               |
       |/api/users/2             | 200               |
        |/api/unknown/2      | 200               |

  