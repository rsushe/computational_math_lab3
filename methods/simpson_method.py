from typing import Callable
from methods.abstract_method import solve_abstract_method

def _calculate(equation: Callable[[float], float], a: float, b: float, partition_value: int):
    h: float = (b - a) / partition_value
    
    sum: float = equation(a) + 4 * equation(a + h) + equation(b)

    for step in range(1, partition_value // 2):
        sum += 2 * equation(a + (2 * step) * h) + 4 * equation(a + (2 * step + 1) * h)
    
    return sum * h / 3


def solve_integral(equation: Callable[[float], float], a: float, b: float, accuracy: float, partition_value: int):
    method_function: Callable[[int], float] = lambda partition_value: _calculate(equation, a, b, partition_value)
    return solve_abstract_method(method_function, partition_value, accuracy, 4)
