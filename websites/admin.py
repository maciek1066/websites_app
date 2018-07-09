from django.contrib import admin
from .models import WebPage, Website, WebsiteCategory

admin.site.register(WebsiteCategory)
admin.site.register(Website)
admin.site.register(WebPage)

