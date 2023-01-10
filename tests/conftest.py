import pytest
import random

@pytest.fixture
def scenario_context(): # target_fixture="context"
    r = str(random.randint(1,2000))
    print('....before ' + r)
    yield { }
    print('....after ' + r)
