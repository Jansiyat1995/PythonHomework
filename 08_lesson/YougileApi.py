import os

import requests
from dotenv import load_dotenv


load_dotenv()


class YougileApi:

    def __init__(self, url):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {os.getenv('YOUGILE_TOKEN')}",
            "Content-Type": "application/json"
        }

    # Создать проект
    def create_project(self, title):
        project = {
            "title": title
        }

        resp = requests.post(
            self.url + "/projects",
            headers=self.headers,
            json=project
        )

        return resp

    # Получить проект по ID
    def get_project(self, project_id):
        resp = requests.get(
            self.url + "/projects/" + str(project_id),
            headers=self.headers
        )

        return resp

    # Изменить проект
    def update_project(self, project_id, title):
        project = {
            "title": title
        }

        resp = requests.put(
            self.url + "/projects/" + str(project_id),
            headers=self.headers,
            json=project
        )

        return resp
