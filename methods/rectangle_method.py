from methods.abstract_method import solve_abstract_method, find_intervals_without_break_points
from equation import Equation
from typing import Callable


def _calculate(equation: Callable[[float], float], a: float, b: float, partition_value: int, offset: float):
    h: float = (b - a) / partition_value

    sum: float = 0
    
    start_x: float = a + offset * h
    
    for step in range(partition_value):
        sum += equation(start_x + step * h) #a + 0.5h + i * h = h * (i + 0.5)
    
    return sum * h


def left(equation: Equation, a: float, b: float, accuracy: float, partition_value: int):
    intervals_without_break_points = find_intervals_without_break_points(equation, a, b)
    
    integral_result: float = 0
    partition_value_result: int = -1

    for i in range(len(intervals_without_break_points) // 2):
        method_function: Callable[[int], float] = lambda partition_value: _calculate(equation.itself, intervals_without_break_points[i * 2], intervals_without_break_points[i * 2 + 1], partition_value, 0)
        current_result, current_partition_value = solve_abstract_method(method_function, partition_value, accuracy, 2)

        integral_result += current_result
        partition_value_result = max(partition_value_result, current_partition_value)
    
    return integral_result, partition_value_result

def middle(equation: Equation, a: float, b: float, accuracy: float, partition_value: int):
    intervals_without_break_points = find_intervals_without_break_points(equation, a, b)
    
    integral_result: float = 0
    partition_value_result: int = -1

    for i in range(len(intervals_without_break_points) // 2):
        method_function: Callable[[int], float] = lambda partition_value: _calculate(equation.itself, intervals_without_break_points[i * 2], intervals_without_break_points[i * 2 + 1], partition_value, 0.5)
        current_result, current_partition_value = solve_abstract_method(method_function, partition_value, accuracy, 2)

        integral_result += current_result
        partition_value_result = max(partition_value_result, current_partition_value)
    
    return integral_result, partition_value_result


def right(equation: Equation, a: float, b: float, accuracy: float, partition_value: int):
    intervals_without_break_points = find_intervals_without_break_points(equation, a, b)
    
    integral_result: float = 0
    partition_value_result: int = -1

    for i in range(len(intervals_without_break_points) // 2):
        method_function: Callable[[int], float] = lambda partition_value: _calculate(equation.itself, intervals_without_break_points[i * 2], intervals_without_break_points[i * 2 + 1], partition_value, 1)
        current_result, current_partition_value = solve_abstract_method(method_function, partition_value, accuracy, 2)

        integral_result += current_result
        partition_value_result = max(partition_value_result, current_partition_value)
    
    return integral_result, partition_value_result
