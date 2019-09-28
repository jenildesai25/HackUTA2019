from flask import Flask, request, Response, json
from db import FireBaseConnection

app = Flask(__name__)


@app.route('/')
def hello():
    connect()

    data = {
        'hello': 'world'
    }
    js = json.dumps(data)

    return Response(js, status=200, mimetype='application/json')


def connect():
    fire_base_connection = FireBaseConnection()
    fire_base_connection.connect_to_db()
    return fire_base_connection


@app.route('/validate-company')
def validate_company():
    data = {
        'validation': False
    }
    if request.method == "GET":
        if 'company_name' in request.args:
            # db connection
            fire_base_connection = connect()
            lstCompanies = fire_base_connection.get_companies()
            if request.args['company_name'].lower() in lstCompanies:
                data = {
                    'validation': True
                }
            # return 'Hello ' + request.args['company_name']
    js = json.dumps(data)
    return Response(js, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
