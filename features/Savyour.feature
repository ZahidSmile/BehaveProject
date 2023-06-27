Feature: Login on savyour
  Background:
    Given Launch chrome browser
    When open savyour homepage
    Then Login with session

  Scenario: Verify Search Field & Search Brand
    When Search Field is Available
    Then Search brand on it