from celery import Celery
from zipfile import ZipFile
import requests
import urllib.request
from io import BytesIO

app = Celery('tasks', broker='amqp://localhost/')


# @app.task
# def download_1m_records(url):
#     response = requests.get(url, stream=True)
#     with zipfile.ZipFile(io.BytesIO(response.content), "r") as zip_ref:
#         zip_ref.extractall()

@app.task
def generator_websites(url):
    url = urllib.request.urlopen(url)

    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            for line in my_zip_file.open(contained_file).readlines():
                yield(line.decode())


# for each_website in generator_websites(url):
#     print(each_website.split(',')[0], each_website.split(',')[1])
