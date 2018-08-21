from django import template
from pages.models import Page

register = template.Library()

def get_page_list():
    pages = Page.objects.all()
    return pages
