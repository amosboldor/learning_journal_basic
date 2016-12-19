"""Views for pyramid."""

from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def home_page(request):
    """View for the home page."""
    imported_text = open(os.path.join(HERE, "data/" 'sample.html')).read()
    return Response(imported_text)


def includeme(config):
    """Include me function."""
    config.add_view(home_page, route_name='home')
