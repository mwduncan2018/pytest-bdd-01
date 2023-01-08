from pytest_bdd import scenario, scenarios, given, when, then, parsers
import pytest
import random

scenarios('../features/zed.feature')

@pytest.fixture
def context(): # target_fixture="context"
    return { }


@given('a random number')
@given('another random number')
def _(context):
    if 'rand_num_list' not in context.keys():
        context.update({'rand_num_list': []})
    context.get('rand_num_list').append(random.randint(1,10))

@when('the numbers are added')
def _(context):
    context.update({'result': sum(context.get('rand_num_list'))})

@then(parsers.parse('the result is less than {max_num:d}'))
def _(context, max_num):
    assert context.get('result') < max_num


@given(parsers.parse('the first name is {first_name}'))
def _(context, first_name):
    context.update({'first_name': first_name})

@given(parsers.parse('the last name is {last_name}'))
def _(context, last_name):
    context.update({'last_name': last_name})

@when('the names are concatenated')
def _(context):
    context.update({'full_name': ' '.join([context.get('first_name'), context.get('last_name')])})

@then(parsers.parse('the full name is {full_name}'))
def _(context, full_name):
    assert full_name == context.get('full_name')
