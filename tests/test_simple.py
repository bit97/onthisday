import pytest


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


# content of test_sysexit.py
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# content of test_class_demo.py
class TestClassDemoInstance:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2
