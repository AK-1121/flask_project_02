import os

from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World ! :)"


@app.route('/ping')
def ping():
    return 'Pong!'

if __name__ == '__main__':
    print('APP_SETTINGS: {}'.format(os.environ['APP_SETTINGS']))
    app.run()
