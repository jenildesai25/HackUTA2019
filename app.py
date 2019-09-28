from flask import Flask, request, Response, json
from db import FireBaseConnection

app = Flask(__name__)


@app.route('/')
def hello():
    data = {
        'hello': 'world'
    }
    js = json.dumps(data)

    connect()

    return Response(js, status=200, mimetype='application/json')


def connect():
    fire_base_connection = FireBaseConnection()
    fire_base_connection.connect_to_db()


if __name__ == '__main__':
    app.run()
