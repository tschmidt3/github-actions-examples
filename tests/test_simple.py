from python_package.simple import simple_add

def test_simple_add():
    a = 1
    b = 2
    actual = simple_add(a,b)
    expected = 3
    assert actual == expected