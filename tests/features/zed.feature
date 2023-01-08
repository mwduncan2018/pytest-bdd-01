Feature: Zed

    Scenario: Add random numbers
        Given a random number 
        And another random number 
        When the numbers are added
        Then the result is less than 100
        And the result is less than 50

    Scenario Outline: Concatenate names
        Given the first name is <first_name>
        And the last name is <last_name>
        When the names are concatenated
        Then the full name is <full_name>

        Examples:
        | first_name | last_name | full_name      |
        | Michael    | Duncan    | Michael Duncan |
        | Travis     | Duncan    | Travis Duncan  |
        | Gail       | Duncan    | Gail Duncan    |
        | Bill       | Duncan    | Bill Duncan    |
        | Eric       | Duncan    | Eric Duncan    |