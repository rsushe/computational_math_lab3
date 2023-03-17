from data_io.data_reader import read_user_choice
from pathlib import Path

def write_data(data: dict):
    output_stream_choice: int = read_user_choice([1, 2], "Введите 1 если данные необходимо вывести в консоль, либо введите 2 если данные необходимо вывести в файл: ")

    if output_stream_choice == 1:
        for key in data:
            print(key, ": ", data[key], sep="")
    else:
        filename: str = input("Введите имя файла: ")
        while not Path(filename).is_file():
            filename: str = input("Файла по такому пути не существует, повторите ввод: ")
        
        write_data_to_file(filename=filename, data=data)


def write_data_to_file(filename: str, data: dict):
    with open(filename, "w") as file:
        for key in data:
            file.write(key + ": " + str(data[key]) + "\n")
        