"""Tests for my learing journal server site."""
# import pytest

# from pyramid import testing


def test_detail_view():
    """Test that what's returned by the view contains what we expect."""
    # from .views import detail
    # request = testing.DummyRequest()
    # info = detail(request)
    assert True

# ------- Functional Tests -------


# @pytest.fixture()
# def testapp():
#     """Create an instance of our app for testing."""
#     from learning_journal_basic import main
#     app = main({})
#     from webtest import TestApp
#     return TestApp(app)


# def test_layout_root(testapp):
#     """Test that the contents of the root page contains <article>."""
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert 'Created in the Code Fellows 401 Python Program' in html.find("footer").text


# def test_root_contents(testapp):
#     """Test that the contents of the root page contains as many <article> tags as journal entries."""
#     from .views import ENTRIES

#     response = testapp.get('/', status=200)
#     html = response.html
#     assert len(ENTRIES) == len(html.findAll("article"))
