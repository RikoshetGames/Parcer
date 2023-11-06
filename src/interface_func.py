from src.savers import *
from src.api import *
from src.vacancy import *


def search_vacancies():
    """Функция поиска вакансий"""
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    print()
    keyword = input("Вы выбрали Поиск вакансий.\n"
                    "Введите ключевое слово для поиска по профессии: ")
    while True:
        pages = input("Введите кол-во страниц, по которым будет осуществлен поиск: ")
        if pages.isdigit():
            break
        else:
            print("Некорректный ввод")
    try:
        pages = int(pages)
        from_hh = hh_api.get_vacancies(keyword, pages)
        from_sj = superjob_api.get_vacancies(keyword, pages)
        print('Найденные вакансии на сайте "HeadHuter":\n')
        for i in from_hh:
            print(i)
        print('Найденные вакансии на сайте "SuperJob":\n')
        for i in from_sj:
            print(i)
        print('отсортировать данные перед записью?')
        while True:
            ans = input('"yes" or "no": ')
            print()
            if ans == 'yes':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh)
                from_all.add_vacancies(from_sj)
                from_all.sort_vacancies_by_salary()
                from_all.save_vacancies()
                break
            elif ans == 'no':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh)
                from_all.add_vacancies(from_sj)
                from_all.save_vacancies()
                break
            else:
                print("Некорректный ввод")

    except ValueError:
        print("Некорректный ввод")

def remove_vacancies():
    """Функция удаления вакансий"""
    try:
        print()
        vacancy_remover = JSONSaver()
        vacancy_remover.remove_vacancies()
        print()
    except FileNotFoundError:
        print('Файл не найден')
    except ValueError:
        print("Некорректный ввод")
