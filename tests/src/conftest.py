import pytest

from tests.src.test_utils.test_app import TestApp


class Services:
    # Define services to be used in tests
    def __init__(self):
        pass


class Clients:
    # Define clients to be used in tests
    def __init__(self):
        pass


@pytest.fixture(scope="function")
def base():
    app = TestApp()
    services = Services()
    clients = Clients()

    with app.app_context():
        app.create_tables()
        yield app, services, clients
        app.clear_database()


@pytest.fixture(scope="function")
def app(base):
    app, _, _ = base
    return app


@pytest.fixture(scope="function")
def services(base):
    _, services, _ = base
    return services


@pytest.fixture(scope="function")
def clients(base):
    _, _, clients = base
    return clients
