Feature: JMeter Smoke Test
  As a tester
  I want to run JMeter smoke test
  So that I can check if the application is working fine

Scenario: Run JMeter Smoke Test
  Given I have JMeter installed
  When I run the JMeter test
  Then JMeter execution should be successful
