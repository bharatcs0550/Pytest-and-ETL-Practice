import pytest
# paramaterization - running the same function/test for different input from the same fixtures to get the multiple outcomes
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
])

def test_add_multiple(a, b, expected):
    assert add(a, b) == expected


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


    # pytest.raises() — testing that your code correctly throws an error
def divide():
    return 10/0

def test_dicide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide()