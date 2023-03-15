Feature: Store: Access Store order

  @API @Regression @Smoke
  Scenario Outline:  GET inventory
        Given the API endpoint <url>
        When I perform a GET request
        Then the response code should be <status_code>


        Examples:
         | url                      | status_code |
         |/store/inventory   | 200              |


