
from src.interface_func import *


def user_interface():
    """Интерфейс приложения"""
    print(f"Добро пожаловать!\n"
          f"Вас приветствует приложение для поиска вакансий.")
    while True:
        print()
        action = input(f"Выберите действие, которое хотите совершить:\n"
                       f"1. Поиск вакансий\n"
                       f"2. Удаление вакансий\n"
                       f"3. Вывести вакансии\n"
                       f"4. Выход\n"                       
                       f"Ввод: ")
        if action == '1':
            search_vacancies()

        elif action == '2':
            remove_vacancies()

        elif action == '3':
            print()
            vacancy_reader = JSONSaver()
            vacancy_reader.read_vacancies()
            print()

        elif action == '4':
            exit()

        else:
            print()
            print("Некорректный ввод")

if __name__ == '__main__':
    user_interface()

