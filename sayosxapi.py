from os import system
from re import escape
from flask import Flask

app = Flask(__name__)


@app.route("/<text>")
def index(text='hello'):
    system('say %s' % escape(text))
    return 'ok'

if __name__ == "__main__":
    app.run(debug=False, port=9000, host='0.0.0.0')
