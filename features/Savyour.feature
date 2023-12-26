Feature: User Navigation on Savyour Website

  Background:
    Given the user launches the Chrome browser
    When the user opens the Savyour website
    Then the user logs in with phone number

  Scenario: Verify HomePage Sections
    Given Instore Banner Available
    When the user navigates to the Home Page
    Then the user checks the visibility of all sections

  Scenario: Verify Search Field and Search Brand
    Given the search field is available
    When the user searches for a brand
    Then the user opens the brand

  Scenario: Verify Brand Detail Page
    #  Verify Brand Detail Page
    When the user opens the brand detail page
    Then Verify Brand Card
    And Verify Banner & breadcrump
    And Order Progress Bar + Max Cashback

    #  Verify Brand Detail Page - About and Specialities
    Then About Section is Visible
    And Specialities Section is Visible
    And You May Also Like Section is Visible

    #  Verify Brand Detail Page - User Ratings
    Then Other User Ratings are Visible

    #  Verify Brand Detail Page - User Reviews
    Then Other Users Reviews are Visible
    And Delete Own Review
    And Write a Review

    #  Verify Brand Detail Page - Comment on Review
    Then Adding Comment on Review
    Then Like Comment
    And Delete Comment if Exist