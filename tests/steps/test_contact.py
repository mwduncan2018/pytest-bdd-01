from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect
import pytest
import time

scenarios('feature')

@pytest.fixture 
def context():
    return { }

@when('the Contact page is viewed')
def _(page: Page):
    time.sleep(1)
    page.goto('https://localhost:44372/ProductList')
    time.sleep(2)

@then('a GitHub link should be provided')
def _():
    pass

@then('the following skills should be listed')
def _():
    pass

@then('the following text should display in the footer')
def _():
    pass