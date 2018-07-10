from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import WebsiteCategory, Website, WebPage
from .forms import WebsiteForm, WebPageForm, WebsiteCategoryForm
from .tasks import generator_websites


class WebsitesListView(View):
    def get(self, request):
        category = request.GET.get("category", None)
        websites = Website.objects.all()
        # category = kwargs.get('category')
        if category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category)
        categories = WebsiteCategory.objects.all()

        url = request.GET.get("url", None)
        if url == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("url")
        elif url == "true":
            websites = Website.objects.all().order_by("url")
        title = request.GET.get("title", None)
        if title == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("title")
        elif title == "true":
            websites = Website.objects.all().order_by("title")
        meta_description = request.GET.get("meta_description", None)
        if meta_description == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("meta_description")
        elif meta_description == "true":
            websites = Website.objects.all().order_by("meta_description")
        alexa_rank = request.GET.get("alexa_rank", None)
        if alexa_rank == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("-alexa_rank")
        elif alexa_rank == "true":
            websites = Website.objects.all().order_by("-alexa_rank")
        date_added = request.GET.get("date_added", None)
        if date_added == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("-date_added")
        elif date_added == "true":
            websites = Website.objects.all().order_by("-date_added")
        date_updated = request.GET.get("date_updated", None)
        if date_updated == "true" and category is not None and category != "":
            websites = Website.objects.all().filter(category__name=category).order_by("-date_updated")
        elif date_updated == "true":
            websites = Website.objects.all().order_by("-date_updated")

        ctx = {
            "category": category,
            "websites": websites,
            "categories": categories,
        }
        return render(
            request,
            "websites.html",
            context=ctx,
        )


class WebsiteDetailView(View):
    def get(self, request, website_id):
        website = Website.objects.get(pk=website_id)
        webpages = website.webpage_set.all()
        ctx = {
            "website": website,
            "webpages": webpages,
        }
        return render(
            request,
            "detail_view.html",
            context=ctx,
        )


class CreateView(View):
    def get(self, request):
        form = WebsiteForm()
        form2 = WebPageForm()
        ctx = {
            "form": form,
            "form2": form2,
        }
        return render(
            request,
            "create_view.html",
            context=ctx
        )

    def post(self, request):
        if "new_website" in request.POST:
            form = WebsiteForm(request.POST)
            if form.is_valid():
                form.save()
        if "new_webpage" in request.POST:
            form2 = WebPageForm(request.POST)
            if form2.is_valid():
                form2.save()
        return redirect("/websites")


class CategoriesView(View):
    def get(self, request):
        categories = WebsiteCategory.objects.all()
        ctx = {
            "categories": categories,
        }
        return render(
            request,
            "categories_view.html",
            context=ctx,
        )

    def post(self, request):
        pass


class CreateCategory(View):
    def get(self, request):
        form = WebsiteCategoryForm()
        ctx = {
            "form": form,
        }
        return render(
            request,
            "create_category.html",
            context=ctx,
        )

    def post(self, request):
        form = WebsiteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/categories_view")

