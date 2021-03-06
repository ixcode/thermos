from flask import Flask
import logging


app = Flask(__name__)


@app.route('/')
def hello_world():
    logging.warning("This is a warning!")
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
