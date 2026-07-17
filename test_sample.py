import pytest

@pytest.fixture
def sample_data():
    return [10 ,20, 30]

def test_sum(sample_data):
    assert sum(sample_data) == 60

def test_max(sample_data):
    assert max(sample_data) == 30   



def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5