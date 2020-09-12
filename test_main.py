import pytest
from unittest.mock import Mock, patch
import inspect
from main import *

# Example Setup function
def setup_function(function):
    print(f"Setting up {function.__name__}")

# Example Teardown function
def teardown_function(function):
    print(f"Tearing down {function.__name__}")

# Example Fixture
@pytest.fixture()
def load_data():
    print("Loaded data")
    data = {
        "Spend": [100, 120, 130, 110, 130, 150, 170],
        "Clicks": [200, 240, 260, 220, 260, 300, 340]
    }
    yield data

# Example Unit Test
def test_process_message():
    assert process('test') == {'message': 'test'}

# Example Unit Test with Fixture
def test_process_with_data(load_data):
    json_data = '{"Spend": [100, 120, 130, 110, 130, 150, 170], "Clicks": [200, 240, 260, 220, 260, 300, 340]}'
    response = {'message': 'test', 'data': load_data}
    assert process('test', json_data) == response

# Example Unit Test with Error
def test_process_with_error():
    with pytest.raises(Exception):
        process('test', "this isn't JSON")

# Config to turn on testing
class TestConfig(DevConfig):
    TESTING = True

# Fixture for creating flask app
@pytest.fixture
def tester():
    app = create_app(TestConfig)
    tester = app.test_client()
    yield tester

# Example Unit Tests with App Client
def test_app_response(tester):
    response = tester.get('/', content_type='application/json')
    assert response.status_code == 200

def test_app_index(tester):
    response = tester.get('/', content_type='application/json')
    assert json.loads(response.data) == {"message": "hello world"}

# Example Integration Tests with a Patch
@patch('main.requests.get')
def test_call_api_response(mock_get):
    mock_get.return_value.status_code = 200
    response = call_api()
    assert response.status_code == 200

@patch('main.requests.get')
def test_call_api_content(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]
    mock_get.return_value.content = todos
    response = call_api()
    print(response.content)
    assert response.content is not None