"""Views for pyramid."""

from pyramid.response import Response
import os


HERE = os.path.dirname(__file__)


def home_list(request):
    """View for the home page."""
    imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    return Response(imported_text)


def detail(request):
    """View for the detail page."""
    imported_text = open(os.path.join(HERE, 'templates/post_detail.html')).read()
    return Response(imported_text)


def create(request):
    """View for create page."""
    imported_text = open(os.path.join(HERE, 'templates/new_entry.html')).read()
    return Response(imported_text)


def update(request):
    """View for update page."""
    imported_text = open(os.path.join(HERE, 'templates/edit_entry.html')).read()
    return Response(imported_text)


def includeme(config):
    """Include me function."""
    config.add_view(home_list, route_name='home')
    config.add_view(detail, route_name='detail')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')
