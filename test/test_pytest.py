import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    assert calculator.fun5(10, 2) == 5.0
    assert calculator.fun5(15, 3) == 5.0
    assert calculator.fun5(-10, 2) == -5.0

def test_fun5_zero_division():
    with pytest.raises(ValueError):
        calculator.fun5(10, 0)

def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 2) == 25
    assert calculator.fun6(10, 0) == 1
    assert calculator.fun6(2, -1) == 0.5

def test_fun7():
    assert calculator.fun7(10, 3) == 1
    assert calculator.fun7(15, 4) == 3
    assert calculator.fun7(20, 5) == 0

def test_fun7_zero_division():
    with pytest.raises(ValueError):
        calculator.fun7(10, 0)

def test_average():
    assert calculator.average([2, 4, 6]) == 4.0
    assert calculator.average([1, 2, 3, 4, 5]) == 3.0
    assert calculator.average([10]) == 10.0

def test_variance():
    result = calculator.variance([1, 2, 3, 4, 5])
    assert result == 2.0

def test_standard_deviation():
    result = calculator.standard_deviation([1, 2, 3, 4, 5])
    assert abs(result - 1.414213) < 0.001
    
