Feature: Partners
    As a customer
    I want to administer
    So that I found the partners

    Scenario: Create a partner
        Given My app has an access token
        When Create a partner with document "1432132123891/0001"
        Then I see "201" as response status code

    Scenario: Update a partner
        Given My app has an access token
        Given Create a partner with document "1432132123891/0002"
        When Update a partner with document "1432132123891/0003"
        Then I see "200" as response status code

    Scenario: Delete a partner
        Given My app has an access token
        Given Create a partner with document "1432132123891/0002"
        When Delete a partner with id "1"
        Then I see "204" as response status code

    Scenario: Update a partner
        Given My app has an access token
        Given Create a partner with document "1432132123891/0002"
        When Patch a partner with id "1"
        Then I see "200" as response status code

    Scenario: find a partner
        Given My app has an access token
        Given Create a partner with document "1432132123891/0002"
        When Find a partner with id "1"
        Then I see "200" as response status code

    Scenario: filter a partner
        Given My app has an access token
        Given Create a partner with document "1432132123891/0002"
        When filter a partner
        Then I see "200" as response status code
