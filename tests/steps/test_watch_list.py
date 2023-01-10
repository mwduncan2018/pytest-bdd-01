from pytest_bdd import scenario, scenarios, given, when, then, parsers

scenarios('../features/watch_list.feature')


@when('entries are viewed')
def _():
    pass

@then('an entry can be created')
def _():
    pass

@then('an entry can be edited')
def _():
    pass

@then('an entry can be read')
def _():
    pass

@then('an entry can be deleted')
def _():
    pass