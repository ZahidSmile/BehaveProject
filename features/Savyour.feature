Feature: Login on savyour
  Background:
    Given Launch chrome browser
    When open savyour homepage
    Then Login with session

  Scenario: Verify HomePage Instore Banner
    When Instore Banner Available

  Scenario: Verify HomePage Sections
    When Home Page Sections Visible
    Then Check Visible Sections See All

  Scenario: Verify HomePage Bachat Deals
    Given Bachat Deals Section Visible

  Scenario: Verify HomePage Trending Brands
    Given Trending Brand Section Visible

  Scenario: Verify Search Field & Search Brand
    Given Search Field is Available
    When Search brand on it
    Then open brand