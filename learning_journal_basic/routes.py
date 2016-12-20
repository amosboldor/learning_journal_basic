"""Routes File."""


def includeme(config):
    """All of the routes for the config."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")