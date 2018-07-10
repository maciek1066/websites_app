"""websites_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from websites.views import (
    CategoriesView,
    WebsitesListView,
    WebsiteDetailView,
    CreateView,
    CreateCategory,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^websites/$', WebsitesListView.as_view(), name="websites"),
    url('^websites/(?P<category>\w+)/$', WebsitesListView.as_view()),
    url('^websites/(?P<category>\w+)/(?P<url>\w+)/$', WebsitesListView.as_view(), name="url"),
    url('^detail_view/(?P<website_id>(\d)+)/$', WebsiteDetailView.as_view(), name="detail_view"),
    url('^create_view/$', CreateView.as_view(), name="create_view"),
    url('^categories_view/$', CategoriesView.as_view(), name="categories_view"),
    url('^create_category/$', CreateCategory.as_view(), name="create_category"),
]
