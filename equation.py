from typing import Callable
from math import sin, cos, exp, log

class Equation:
    itself: Callable[[float], float]
    primordial: Callable[[float], float]
    string_representation: str

    def __init__(self, itself: Callable[[float], float], primordial: Callable[[float], float], string_representation: str) -> None:
        self.itself = itself
        self.primordial = primordial
        self.string_representation = string_representation


first_equation = Equation(lambda x: -1.4 * x ** 3 - 0.9 * x ** 2 + 10.67 * x - 2.34, lambda x: -0.35 * x ** 4 - 0.3 * x ** 3 + 5.335 * x ** 2 - 2.34 * x, "-1.4x^3 - 0.9x^2 + 10.67x - 2.34")
second_equation = Equation(lambda x: exp(x) * x, lambda x: x * exp(x) - exp(x), "e^x * x")
third_equation = Equation(lambda x: sin(x) - cos(x) + 1.5 * x, lambda x: -cos(x) - sin(x) + 3 * x ** 2 / 4, "sin(x) - cos(x) + 1.5x")
fourth_equation = Equation(lambda x: 1 / x, lambda x: log(abs(x)), "1 / x")
fifth_equation = Equation(lambda x: x / (x ** 2 - 1), lambda x: log(abs(x ** 2 - 1)) / 2, "x / (x^2 - 1)")

equations: list[Equation] = [
    first_equation,
    second_equation,
    third_equation,
    fourth_equation,
    fifth_equation
]