*** Settings ***
Resource        Calc_keywords.resource

*** Test Cases ***
Test Calculator With BDD Syntax
    Given The Calculator Is Running
    When The User Enters The Term "12 * 2"
    And The User Triggers The Calculation
    Then The Result Should Be "24"
    And The Test Finished

