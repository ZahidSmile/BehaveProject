Feature: Verify Brand Detail Page

  Background:
  Given Launch chrome browser
  When open savyour homepage
  Then Login with session

Scenario: Verify Brand Detail Page

  When Instore Page Open
  Then Verify Brand Card
  And Verify Banner & breadcrump
  And Order Progress Bar + Max Cashback

Scenario: Verify Brand Detail Page - About and Specialities

  When Instore Page Open
  Then About Section is Visible
  And Specialities Section is Visible
  And You May Also Like Section is Visible

Scenario: Verify Brand Detail Page - User Ratings

  When Instore Page Open
  Then Other User Ratings are Visible

Scenario: Verify Brand Detail Page - User Reviews

  When Instore Page Open
  Then Other Users Reviews are Visible
  And Delete Own Review
  And Write a Review

Scenario: Verify Brand Detail Page - Comment on Review

  When Instore Page Open
  Then Adding Comment on Review
#  And Delete Comment if Exist

Scenario: Verify Brand Detail Page - Like Comment & Review

  When Instore Page Open
#  Then Like Comment & Review