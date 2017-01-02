"""Tests for my learing journal server site."""
import pytest

from pyramid import testing
from .views import ENTRIES


# ------- Unit Tests -------

def test_home_list_view():
    """Test that home view returns dictionary of data."""
    from .views import home_list
    request = testing.DummyRequest()
    info = home_list(request)
    assert info["posts"] == ENTRIES


def test_detail_view():
    """Test that detail view returns correct entry."""
    from .views import detail
    request = testing.DummyRequest()
    request.matchdict['id'] = 1
    info = detail(request)
    assert info['post'] == ENTRIES[0]


# not testing create view because it returns an empty dictionary


def test_update_view():
    """Test that update view returns correct entry."""
    from .views import update
    request = testing.DummyRequest()
    request.matchdict['id'] = 1
    info = update(request)
    assert info['post'] == ENTRIES[0]

# ------- Functional Tests -------


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_home_list_route(testapp):
    """Test that the home page route returns html with li entries."""
    response = testapp.get('/', status=200)
    html = response.html
    assert html.find_all('li')[-2].a.getText() == ENTRIES[0]['title']
    assert html.find_all('li')[-1].a.getText() == ENTRIES[1]['title']


def test_detail_route(testapp):
    """Test that the detail route returns html with title and body of entry."""
    response = testapp.get('/journal/1', status=200)
    html = response.html
    assert html.find('main').h1.getText() == ENTRIES[0]['title']
    assert ENTRIES[0]['body'] in html.find('main').p.getText()


def test_new_entry_route(testapp):
    """Test that new-entry route returns html with input and textarea."""
    response = testapp.get('/journal/new-entry', status=200)
    html = response.html
    assert html.textarea
    assert html.input


def test_update_route(testapp):
    """Test that the update route puts exising entry in input and texarea."""
    response = testapp.get('/journal/1/edit-entry', status=200)
    html = response.html
    assert html.textarea.getText() == ENTRIES[0]['body']
    assert html.input.get('value') == ENTRIES[0]['title']
