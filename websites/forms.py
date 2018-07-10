from django.forms import ModelForm
from websites.models import WebsiteCategory, Website, WebPage


class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = "__all__"


class WebPageForm(ModelForm):
    class Meta:
        model = WebPage
        fields = "__all__"
