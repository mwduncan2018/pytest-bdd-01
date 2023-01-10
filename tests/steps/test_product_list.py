from pytest_bdd import scenario, scenarios, given, when, then, parsers

scenarios('../features/product_list.feature')


@when('products are viewed')
def _():
    pass

@then('a product can be created')
def _():
    pass

@then('a product can be edited')
def _():
    pass

@then('a product can be read')
def _():
    pass

@then('a product can be deleted')
def _():
    pass