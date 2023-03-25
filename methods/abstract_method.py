from typing import Callable

def solve_abstract_method(method_function: Callable[[int], float], partition_value: int, accuracy: float, accuracy_order: int):

    previous_result: float = 1e10
    current_result: float = method_function(partition_value)

    while abs(current_result - previous_result) / (2 ** accuracy_order - 1) >= accuracy:
        partition_value *= 2

        previous_result = current_result
        current_result = method_function(partition_value)
    
    return current_result, partition_value
