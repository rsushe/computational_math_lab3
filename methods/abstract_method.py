from typing import Callable
from equation import Equation
import math

def solve_abstract_method(method_function: Callable[[int], float], partition_value: int, accuracy: float, accuracy_order: int):

    previous_result: float = 1e10
    current_result: float = method_function(partition_value)

    while abs(current_result - previous_result) / (2 ** accuracy_order - 1) >= accuracy:
        partition_value *= 2

        previous_result = current_result
        current_result = method_function(partition_value)
    
    return current_result, partition_value


def find_intervals_without_break_points(equation: Equation, a: float, b: float, step: float = 0.01):
    intervals_without_break_points = []

    if is_break_point(equation, a):
        check_for_convergence(equation, a)
        intervals_without_break_points.append(a + step)
    else:
        intervals_without_break_points.append(a)
    
    current_x = a + step
    while current_x < b:
        if is_break_point(equation, current_x):
            check_for_convergence(equation, current_x)
            intervals_without_break_points.append(current_x - step)
            intervals_without_break_points.append(current_x + step)
        current_x += step
    
    if is_break_point(equation, b):
        check_for_convergence(equation, b)
        intervals_without_break_points.append(b - step)
    else:
        intervals_without_break_points.append(b)

    return intervals_without_break_points


def is_break_point(equation: Equation, x: float):
    try:
        result = equation.itself(x)
        if abs(result) > 1e10:
            return True
    except Exception:
        return True
    return False


def check_for_convergence(equation: Equation, x: float):
    try:
        result = equation.primordial(x)
        if abs(result) > 1e10:
            raise ValueError("Интеграл не сходится")
    except ValueError:
        raise ValueError("Интеграл не сходится")