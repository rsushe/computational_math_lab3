from methods.abstract_method import solve_abstract_method
from typing import Callable


def _calculate(equation: Callable[[float], float], a: float, b: float, partition_value: int, offset: float):
    h: float = (b - a) / partition_value

    sum: float = 0
    
    start_x: float = a + offset * h
    
    for step in range(partition_value):
        sum += equation(start_x + step * h) #a + 0.5h + i * h = h * (i + 0.5)
    
    return sum * h


def left(equation: Callable[[float], float], a: float, b: float, accuracy: float, partition_value: int):

    method_function: Callable[[int], float] = lambda partition_value: _calculate(equation, a, b, partition_value, 0)
    return solve_abstract_method(method_function, partition_value, accuracy, 1)


def middle(equation: Callable[[float], float], a: float, b: float, accuracy: float, partition_value: int):

    method_function: Callable[[int], float] = lambda partition_value: _calculate(equation, a, b, partition_value, 0.5)
    return solve_abstract_method(method_function, partition_value, accuracy, 1)


def right(equation: Callable[[float], float], a: float, b: float, accuracy: float, partition_value: int):

    method_function: Callable[[int], float] = lambda partition_value: _calculate(equation, a, b, partition_value, 1)
    return solve_abstract_method(method_function, partition_value, accuracy, 1)
