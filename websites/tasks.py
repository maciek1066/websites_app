from celery import Celery, shared_task
from zipfile import ZipFile
import urllib.request
from io import BytesIO

app = Celery('tasks', broker='amqp://localhost/')


# @app.task()
@shared_task
def generator_websites(url):
    url = urllib.request.urlopen(url)

    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            for line in my_zip_file.open(contained_file).readlines():
                yield(line.decode())
                for each_website in generator_websites(url):
                    print(each_website.split(',')[0], each_website.split(',')[1])
