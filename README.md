

```
# Print
pytest .\tests\steps\test* -s

# Parallel (pytest-xdist)
pytest .\tests\steps\test* -n 10
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