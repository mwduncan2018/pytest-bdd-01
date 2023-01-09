
```
# Parallel (pytest-xdist)
pytest .\tests\steps\test* -n 10
```

```
# Print
pytest .\tests\steps\test* -s
```

```
# Link features
scenarios('../features/name_of.feature')
```

```
# Scenario Context
@pytest.fixture
def context():
    return { }

@given('scenario context is used')
def _(context):
    pass
```