Feature: All Delete Test Cases

   Scenario Outline: Delete request
        Given the API endpoint <url>
        When I perform DELETE request
        Then the response code should be <status_code>

        Examples:
        |url                            | status_code |
        |/api/users/2              | 204             |




