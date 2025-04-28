# language: en
Feature: Home Page
  Scenario: Accessing the home page
    Given the Flask app is running
    When I visit the home page
    Then I should see "Hello, Flask!"