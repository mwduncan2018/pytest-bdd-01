from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
import re
import pytest
import time

scenarios('../features/contact.feature')

@pytest.fixture 
def scenario_context():
    return { }

@when('the Contact page is viewed')
def _(scenario_context: dict, page: Page):
    page.goto('https://localhost:44372/Home/Contact')

@then(parsers.parse('the following text should display in the footer{footer_text}'))
def _(scenario_context: dict, page: Page, footer_text: str):
    footer_text = footer_text.replace('"','').replace('\n','')
    expect(page.get_by_text(footer_text)).to_be_visible()

@then(parsers.parse('a GitHub link should be provided{github_link}'))
def _(scenario_context: dict, page: Page, github_link: str):
    github_link = github_link.replace('"','').replace('\n','')
    assert page.locator('#github a').get_attribute('href') == github_link
    

@then(parsers.parse('the following {skill} should be listed'))
def _(scenario_context: dict, page: Page, skill: str):
    expect(page.get_by_text(skill, exact=True)).to_be_visible()