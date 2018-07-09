from django.shortcuts import render
from django.views import View
from .models import WebsiteCategory, Website, WebPage


def websites_list_view(request, category=""):
    if request.method == "GET":
        websites = Website.objects.all()
        categories = WebsiteCategory.objects.all()

    if request.GET.get(category):
        category = request.GET.get(category)
        WebsiteCategory.objects.get(category=category)
        websites = Website.objects.filter(category=category)
    return render(request, "websites.html", {
        'websites': websites,
        'categories': categories,
    })