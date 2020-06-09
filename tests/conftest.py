
import pytest

from routes import server

@pytest.fixture
def app():
    app = server
    return app

@pytest.fixture(scope='function')
def client(request, app):
    client = app.test_client()
    return client
