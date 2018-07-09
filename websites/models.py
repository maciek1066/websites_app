from django.db import models

# Website:
#     url
#     title
#     meta_description
#     alexa_rank
#     category - FK WebsiteCategory
#     date_added
#     date_updated


# WebsiteCategory:
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
