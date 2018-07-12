from celery import Celery, shared_task
from zipfile import ZipFile
import urllib.request
from io import BytesIO
from .models import WebsiteCategory, Website, WebPage
import bs4
from urllib.request import urlopen as u_req
from bs4 import BeautifulSoup as soup


app = Celery('tasks', broker='amqp://localhost/')


# @app.task()
@shared_task
def get_websites(url):
    url = urllib.request.urlopen(url)
    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            for line in my_zip_file.open(contained_file).readlines():
                #  link + rank from zip file
                website = line.decode().split(',')[1]
                position = line.decode().split(',')[0]
                # TestModel.objects.create(website=website, position=position)

                #  scraping for info
                url = "http://"+website
                u_client = u_req(url)
                page_html = u_client.read()
                u_client.close()
                page_soup = soup(page_html, "html.parser")
                if page_soup.find("title"):
                    title = page_soup.find("title").text
                else:
                    title = "no title"
                meta = page_soup.find("meta", {"name": "description"})
                meta_description = meta["content"] if meta else "no meta description given"
                category = WebsiteCategory.objects.get(name="test")
                new_object = Website.objects.create(
                    url=url,
                    title=title,
                    meta_description=meta_description,
                    alexa_rank=position,
                    category=category,
                    )
