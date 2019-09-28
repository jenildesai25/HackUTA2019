from flask import Flask,request, Response,json

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        'hello'  : 'world'
    }
    js = json.dumps(data)

    return Response(js, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
