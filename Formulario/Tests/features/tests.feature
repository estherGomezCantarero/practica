Feature: tests


  Scenario: Pressing Submit
    When I click Submit
    Then I see text area empty

  Scenario: Introduce text
    Given I introduce string
    When I click Submit
    Then I see text area empty

  Scenario: Introduce specific string 1
    Given I introduce string with fa 3 times and h 1 time
    When I click Submit
    Then I see text area empty
    And I see string result for h 4 times and fa 3 times

  Scenario: Introduce specific string 2
    Given I introduce string with fa 5 times ,h 4 times , v 6 times , j 2 times and k 1 time
    When I click Submit
    Then I see text area empty
    And I see string result for v six times, fa 5 times, h 4 times, j 2 times and k 1 time

  Scenario: Introduce specific string 3
    Given I introduce string with word and dots
    When I click Submit
    Then I see text area empty
    And

  Scenario: Introduce string empty
    Given I introduce string empty
    When I click Submit
    Then I see string result for fa 1 time

