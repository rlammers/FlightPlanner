"""Integration tests for the Bottle web application."""

import json
from wsgiref.util import setup_testing_defaults

from bottle import default_app

import app


def test_imported_app_serves_flight_schedule():
    """The imported WSGI application has initialized route dependencies."""
    assert app.AIRPORT_SERVICE is not None

    environ = {}
    setup_testing_defaults(environ)
    environ['PATH_INFO'] = '/flightschedule'
    environ['REQUEST_METHOD'] = 'GET'
    response_status = None

    def start_response(status, _headers, _exc_info=None):
        nonlocal response_status
        response_status = status

    response_body = b''.join(default_app()(environ, start_response))
    payload = json.loads(response_body)

    assert response_status == '200 OK'
    assert payload['type'] == 'FeatureCollection'
    assert payload['features']
