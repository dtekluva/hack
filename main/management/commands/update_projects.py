from django.core.management.base import BaseCommand
from main.models import *
import requests


class Command(BaseCommand):
    help = 'check for new_projects'

    def handle(self, *args, **kwargs):
        # try:

        url = 'https://kc.kobotoolbox.org/api/v1/data'

        headers = {'content-type': 'application/json', 'Authorization':'Token bcc979086ef1de7e787427fd1827abff776e1cd3'}

        response = requests.get(url, headers = headers)
        projects = response.json()

        for uid, project in enumerate(projects):
            project_title = project["title"]
            project_url = project["url"]
            
            project, status = Project.objects.get_or_create(title = project_title, data_url = project_url)

            if status: project.set_date_added(); project.add_data_set()
            

        self.stdout.write("Update datasets Successfull")

        # except:
            
        #     self.stdout.write("Update datasets Failed")              