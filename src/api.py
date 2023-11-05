import requests
import os
from dotenv import load_dotenv
from src.vacancy import Vacancy


class JobAPI:
    """Абстрактный класс для хранения информации из API"""

    def __init__(self):
        pass

    def get_vacancies(self, name_job):
        pass


class HeadHunterAPI(JobAPI):
    "Класс для хранения информации из API с сайта HH"

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job, pages):
        """Хранение вакансий отдельным классом"""
        url = self.url
        ans = []
        for item in range(pages):
            param = {'text': name_job, 'per_page': '3', 'page': item}
            reques = requests.get(url, params=param)
            element = reques.json()
            for job in element['items']:
                job_id = job['id']
                job_url = job['alternate_url']
                name = job['name']
                if not ((job['salary'] is None) or (job['salary']['from'] is None)):
                    salary_from = job['salary']['from']
                    salary_to = job['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                if not (job['address'] is None):
                    city = job['address']['city']
                else:
                    city = None
                vacanc = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                ans.append(vacanc)
        return ans


class SuperJobAPI(JobAPI):
    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        load_dotenv()
        self.api_key = os.getenv('API_SUPERJOB')

    def get_vacancies(self, name_job, pages):
        url = self.url
        ans = []
        head = {'Host': 'api.superjob.ru',
                'X-Api-App-Id': self.api_key
                }
        for item in range(pages):
            param = {'keyword': name_job, 'count': 3, 'page': item}
            reques = requests.get(url, params=param, headers=head)
            element = reques.json()
            for j in element['objects']:
                job_id = str(j['id'])
                job_url = j['link']
                name = j['profession']
                salary_from = j['payment_from']
                salary_to = j['payment_to']
                if j['address'] is None:
                    city = None
                else:
                    city = j['address'].split(',')[0]
                vacanc = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                ans.append(vacanc)
        return ans