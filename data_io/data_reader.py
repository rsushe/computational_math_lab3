from equation import equations, Equation

class InputData:
    equation: Equation
    method: int
    integration_interval: list[float]
    accuracy: float
    partition_value: int

    
def read_user_choice(range: list[int], user_text: str):
    user_choice: int = -1
    while user_choice not in range:
        try:
            user_choice: int = int(input(user_text))      
        except ValueError:
            continue
    return user_choice


def read_input_data():
    input_data: InputData = InputData()

    input_data.equation = read_single_equation()
    
    input_data.method = read_user_choice([1, 2, 3, 4, 5], "Введите 1 чтобы выбрать метод Хорд, 2 чтобы выбрать метод секущих или 3 чтобы выбрать метод простой итерации: ")    

    input_data.integration_interval = read_integration_interval()

    input_data.accuracy = read_accuracy()

    input_data.partition_value = 4

    return input_data


def read_single_equation():
    for i in range(len(equations)):
        print("{}: {}".format(i + 1, equations[i].string_representation))
    
    user_choice: int = read_user_choice([i + 1 for i in range(len(equations))], "Введите номер желаемого выражения: ")

    return equations[user_choice - 1]

def read_method():
    print("1 - Метод левых прямоугольников")
    print("2 - Метод средних прямоугольников")
    print("3 - Метод правых прямоугольников")
    print("4 - Метод трапеций")
    print("5 - Метод Симпсона")
    
    method: int = read_user_choice([1, 2, 3, 4, 5], "Введите номер желаемого метода решения интегралов: ")

    return method


def read_integration_interval():
    print("Введите начальную границу интервала: ", end="")
    while True:
        try:
            interval_start: float = float(input().replace(",", "."))
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue
    
    print("Введите конечную границу интервала: ", end="")
    while True:
        try:
            interval_end: float = float(input().replace(",", "."))
            if interval_end <= interval_start:
                print("Конец интервала должен быть строго больше чем начало интервала, повторите ввод: ", end="")
                continue
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue
    return [interval_start, interval_end]


def read_accuracy():
    print("Введите желаемую точность: ", end="")
    while True:
        try:
            accuracy: float = float(input().replace(",", "."))
            if accuracy <= 0:
                print("Точность не может быть отрицательной, повторите ввод: ", end="")
                continue
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue

    return accuracy
    