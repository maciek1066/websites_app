from django.db import models


class WebsiteCategory(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    meta_description = models.CharField(max_length=512)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.url


class WebPage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    URL = models.CharField(max_length=128, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=32)
    meta_description = models.CharField(max_length=128)


