"""Views for pyramid."""

from pyramid.view import view_config
ENTRIES = [
    {
        "title": "Monday 12/19: Day 12",
        "id": 1,
        "published_on": "Dec 20, 2016",
        "body": """Today we got to learn about the python framework pyramid and it was not that hard to setup just tedious.
        We also had to implement a Deque and we imported double linked list to do this.
        Today was easy compared to other days
        """
    },
    {
        "title": "Entry 2",
        "id": 2,
        "creation_date": "Dec 21, 2016",
        "body": "I learned some stuff about some other stuff. Also Maelle is an awesome partner! Yay her!"
    },
]


@view_config(route_name="home", renderer="templates/index.jinja2")
def home_list(request):
    """View for the home page."""
    # imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    # # return Response(imported_text)
    return {"posts": ENTRIES}


@view_config(route_name="detail", renderer="templates/post_detail.jinja2")
def detail(request):
    """View for the detail page."""
    # request.matchdict.['id']
    return {"post": ENTRIES[int(request.matchdict['id']) - 1]}


@view_config(route_name="create", renderer="templates/new_post_form.jinja2")
def create(request):
    """View for create page."""
    return 'request'


@view_config(route_name="update", renderer="template")
def update(request):
    """View for update page."""

