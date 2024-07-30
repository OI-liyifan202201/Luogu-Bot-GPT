import json
import time
import flask
import requests

app = flask.Flask(__name__)

process = 2


def forward(data):
    global process
    while process == 0:
        time.sleep(0.1)
    process -= 1
    headers = json.loads(data['headers'])
    headers['User-Agent'] = ''
    if json.loads(data['json']) != {}:
        response = requests.request(
            method=data['method'],
            url=data['url'],
            headers=headers,
            json=json.loads(data['json']),
        )
    else:
        response = requests.request(
            method=data['method'],
            url=data['url'],
            headers=headers,
        )
    process += 1
    return flask.Response(
        response=response.content,
        status=response.status_code,
    )


@app.route('/', methods=['POST'])
def root():
    return forward(flask.request.get_json())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
