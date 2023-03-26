from data_io.data_reader import InputData, read_input_data
from methods import rectangle_method, simpson_method, trapezoid_method
from equation import Equation

if __name__ == "__main__":
    try:

        input_data: InputData = read_input_data()

        equation: Equation = input_data.equation
        a: float = input_data.integration_interval[0]
        b: float = input_data.integration_interval[1]
        accuracy: float = input_data.accuracy
        partition_value: int = input_data.partition_value
        method: int = input_data.method

        match method:
            case 1:
                integral_result, partition_value = rectangle_method.left(equation, a, b, accuracy, partition_value)
            case 2:
                integral_result, partition_value = rectangle_method.middle(equation, a, b, accuracy, partition_value)
            case 3:
                integral_result, partition_value = rectangle_method.right(equation, a, b, accuracy, partition_value)
            case 4:
                integral_result, partition_value = trapezoid_method.solve_integral(equation, a, b, accuracy, partition_value)
            case 5:
                integral_result, partition_value = simpson_method.solve_integral(equation, a, b, accuracy, partition_value)

        print("Результат вычисления = {}".format(integral_result))
        print("Количество разбиений отрезка = {}".format(partition_value))

    except Exception as e:
        print(str(e))
        print("Программа завершена")
    except KeyboardInterrupt:
        print("Программа завершена из-за неправильного ввода")