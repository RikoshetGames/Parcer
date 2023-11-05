from abc import ABC, abstractmethod
from src.vacancy import *
import json


class Saver(ABC):
    """Абстрактный класс для редактирования и обработки списка вакансий"""
    @abstractmethod
    def save_vacancies(self):
        """Метод для сохранения вакансий"""
        pass

    @abstractmethod
    def read_file(self):
        """Метод для считывания данных из файла JSON"""
        pass

    @abstractmethod
    def read_vacancies(self):
        """Метод для вывода вакансий"""
        pass

    @abstractmethod
    def remove_vacancies(self):
        """Метод для удаления вакансий"""
        pass


class JSONSaver(Vacancies, Saver):
    """Класс для обработки списка вакансий в JSON формате"""
    FILE_PATH = 'vacancies.json'
    def save_vacancies(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as fh:
            json.dump(self.to_list_dict(), fh, indent=4, ensure_ascii=False)

    def read_file(self):
        with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def read_vacancies(self):
        data = self.read_file()
        for i, item in enumerate(data):
            print(f"{i + 1}. {item['name']}")
        print()

    def remove_vacancies(self):
        data = self.read_file()
        for i, item in enumerate(data):
            print(f"{i + 1}. {item['name']}")
        print()

        index_to_remove = int(input("Введите номер вакансии для удаления: ")) - 1

        if index_to_remove < 0 or index_to_remove >= len(data):
            print("Некорректный номер вакансии.")
            return

        removed_dict = data.pop(index_to_remove)
        print(removed_dict)

        with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)