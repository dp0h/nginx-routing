from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'app1:root'

@app.route('/api')
def api():
    return 'app1:api'

@app.route('/api/api1')
def api_api1():
    return 'app1:api:api1'

@app.route('/api/api2')
def api_api2():
    return 'app1:api:api2'
