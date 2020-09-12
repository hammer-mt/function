# Import relevant libraries
from flask import jsonify
import json
import requests

# Define support or helper functions
def process(message, data=None):
    if data:
        return {'message': message, 'data': json.loads(data)}
    else:
        return {'message': message}

# Call 3rd party APIs
def call_api():
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    return response

# This is where the main function runs
def main(request):
    message = request.args.get('message') or 'hello world'
    data = request.args.get('data')
    
    response = process(message, data)
    return jsonify(response)

# App factory so we can test
class DevConfig():
    SECRET_KEY = 'youwillneverguess'
    FLASK_ENV = 'development'
    DEBUG = True

def create_app(config_obj):
    # create and configure the app
    from flask import Flask, request
    app = Flask(__name__)    
    app.config.from_object(config_obj)
    app.route('/')(lambda: main(request))
    return app

# If run via CLI for development
if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(debug=True)