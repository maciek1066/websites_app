from celery import Celery, shared_task
from zipfile import ZipFile
import urllib.request
from io import BytesIO
from .models import TestModel

app = Celery('tasks', broker='amqp://localhost/')


# @app.task()
@shared_task
def get_websites(url):
    url = urllib.request.urlopen(url)
    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            for line in my_zip_file.open(contained_file).readlines():
                website = line.decode().split(',')[1]
                position = line.decode().split(',')[0]
                TestModel.objects.create(website=website, position=position)

