from django.db import models

# Website:
#     url
#     title
#     meta_description
#     alexa_rank
#     category - FK WebsiteCategory
#     date_added
#     date_updated


class Website(models.Model):
    url = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    meta_description = models.CharField(max_length=32)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory)


class WebsiteCategory(models.Model):
    pass
#     name
#     description
#     date_added
#     date_updated
#     count

# WebPage:
#     website - FK Website
#     URL - unikalny
#     date_added
#     date_updated
#     title
#     meta_description
