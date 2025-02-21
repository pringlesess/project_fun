import requests
import json
from flask import Flask

app = Flask(__name__)

def getjoke():
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers={'Accept': 'application/json'})
    return response.json().get('joke')

@app.route('/dadjoke')
def dadjoke():
    return getjoke()

@app.route('/')
def index():
    return "Nothing Here"

@app.route('/services')
def services():
    services = [
        "User Authentication",
        "Database Management",
        "API Gateway",
        "File Storage",
        "Email Notification",
        "Logging Service",
        "Monitoring Service"
    ]
    return json.dumps(services)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

def main():
    print("Hello World")
    print(getjoke())
