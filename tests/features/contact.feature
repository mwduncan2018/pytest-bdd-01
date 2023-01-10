@contact
Feature: Contact

	Scenario: Duncan safe product
		When the Contact page is viewed
		Then the following text should display in the footer
			"""
			(Duncan Safe Product!)
			"""

	Scenario: GitHub link
		When the Contact page is viewed
		Then a GitHub link should be provided
			"""
			https://github.com/mwduncan2018
			"""

	Scenario Outline: Technical skills are displayed
		When the Contact page is viewed
		Then the following <skill> should be listed

		Examples:
		| skill                       |
		| C# SpecFlow                 |
		| Java Cucumber               |
		| Docker                      |
		| Docker Compose              |
