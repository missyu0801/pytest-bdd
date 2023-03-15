Feature: Store: Access Store order

   @E2E @API @Regression @Smoke
   Scenario Outline: POST Request
        Given the API endpoint <url>
        When I input a json '<path>' file
        And I perform a POST request
        And I stored the value from keyword <key> to <container>
        Then the response code should be <status_code>
        And Verify container key <key> has value <container>
        And  Verify response content <petId> should be <value1>
        And  Verify response content <qty> should be <value2>

        Examples:
        |url                           | path                                     | petId | value1 | qty           |  value2 | key | container | status_code |
        |/store/order             | ./json_data/store_data.json  | petId | 22        |  quantity  | 12         |id    | storage    |200                |

  @E2E @API @Regression @Smoke
   Scenario Outline:  GET Request
        Given the API endpoint <url>
        When I perform request chaining with method <method>
        Then the response code should be <status_code>
        Then Verify container key <key> has value <container>

        Examples:
         | url                 | container | key | status_code | method|
          |/store/order   | storage    | id    | 200              | Get     |

  @E2E @API @Regression @Smoke
  Scenario Outline:  Delete Request
        Given the API endpoint <url>
        When I perform request chaining with method <method>
        Then the response code should be <status_code>


        Examples:
         | url                 |  status_code | method |
         |/store/order   |  200               | delete |

  @E2E @API @Regression @Smoke @Negative
  Scenario Outline:  GET the deleted Request
        Given the API endpoint <url>
        When I perform request chaining with method <method>
        Then the response code should be <status_code>
        And Verify response message should be '<message>'

        Examples:
         | url                 | status_code | message            | method |
         |/store/order    | 404              |  Order not found| GET       |

  @E2E @API @Regression @Smoke
  Scenario Outline: Create new POST Request
        Given the API endpoint <url>
        When I input a json '<path>' file
        And I change input of key <petId> and value <value1>
        And I change input of key <qty> and value <value2>
        And I perform a POST request
        And I stored the value from keyword <key> to <container>
        Then the response code should be <status_code>
        And Verify container key <key> has value <container>
        And Verify response content <petId> should be <value1>
        And Verify response content <qty> should be <value2>

        Examples:
        |url                           | path                                     | petId | value1 | qty           |  value2 | key | container | status_code |
        |/store/order             | ./json_data/store_data.json  | petId | 32        |  quantity  | 100       |id    | storage    |200                |