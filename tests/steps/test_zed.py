from pytest_bdd import scenario, scenarios, given, when, then, parsers
import random

scenarios('../features/zed.feature')


@given('a random number')
@given('another random number')
def _(scenario_context):
    if 'rand_num_list' not in scenario_context.keys():
        scenario_context.update({'rand_num_list': []})
    scenario_context.get('rand_num_list').append(random.randint(1,10))

@when('the numbers are added')
def _(scenario_context):
    scenario_context.update({'result': sum(scenario_context.get('rand_num_list'))})

@then(parsers.parse('the result is less than {max_num:d}'))
def _(scenario_context, max_num):
    assert scenario_context.get('result') < max_num


@given(parsers.parse('the first name is {first_name}'))
def _(scenario_context, first_name):
    scenario_context.update({'first_name': first_name})

@given(parsers.parse('the last name is {last_name}'))
def _(scenario_context, last_name):
    scenario_context.update({'last_name': last_name})

@when('the names are concatenated')
def _(scenario_context):
    scenario_context.update({'full_name': ' '.join([scenario_context.get('first_name'), scenario_context.get('last_name')])})

@then(parsers.parse('the full name is {full_name}'))
def _(scenario_context, full_name):
    assert full_name == scenario_context.get('full_name')
