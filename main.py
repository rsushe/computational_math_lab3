from data_io.data_reader import InputData, read_input_data
from methods import rectangle_method, simpson_method, trapezoid_method
from typing import Callable

if __name__ == "__main__":
    try:

        input_data: InputData = read_input_data()

        equation: Callable[[float], float] = input_data.equation.itself
        integration_interval: list[float] = input_data.integration_interval
        accuracy: float = input_data.accuracy
        method: int = input_data.method

        answer_data: dict = None

    except Exception as e:
        print(str(e))
        print("Программа завершена")
    except KeyboardInterrupt:
        print("Программа завершена из-за неправильного ввода")