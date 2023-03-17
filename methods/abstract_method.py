from typing import Callable

def solve_abstract_integral(method_function: Callable[[float, float, float], float], a: float, b: float, 
                       accuracy: float, partition_value: int):
    h = calculate_h(a, b, partition_value)

    previous_result = 1e10
    current_result = method_function(a, b, h)

    while abs(current_result - previous_result) >= accuracy:

        partition_value *= 2
        h = calculate_h(a, b, partition_value)

        previous_result = current_result
        current_result = method_function(a, b, h)
    
    return current_result


def calculate_h(a: float, b: float, partition_value: int):
    return (b - a) / partition_value
