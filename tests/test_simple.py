from python_package.simple import simple_add
import pytest


@pytest.mark.parametrize("a,b, expected", [(1, 2, 3), (-1, -2, -3)])
def test_simple_add(a, b, expected):
    assert simple_add(a, b) == expected
