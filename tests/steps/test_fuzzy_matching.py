from pytest_bdd import scenario, scenarios, given, when, then, parsers

scenarios('../features/fuzzy_matching.feature')


@given(parsers.parse('a product is added with manufacturer {productManufacturer} and model {productModel}'))
def _(productManufacturer, productModel):
    pass

@then(parsers.parse('an entry is added with manufacturer {entryManufacturer} and model {entryModel}'))
def _(entryManufacturer, entryModel):
    pass

@when(parsers.parse('fuzzy matching is enabled'))
def _():
    pass

@then(parsers.parse('the product with manufacturer {productManufacturer} and model {productModel} is a standard match'), converters={"productManufaturer": str, "productModel": str})
def _(productManufacturer, productModel):
    pass

@then(parsers.parse('the product with manufacturer {productManufacturer} and model {productModel} is not a match'))
def _(productManufacturer, productModel):
    pass

@then(parsers.parse('the product with manufacturer {productManufacturer} and model {productModel} is a fuzzy match'))
def _(productManufacturer, productModel):
    pass