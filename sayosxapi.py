from os import system
from commands import getoutput
from re import sub, match
from flask import Flask
import logging


app = Flask(__name__)


def sanitize(text):
    text = sub('[-_\+]+', ' ', text)
    text = sub('[^a-zA-Z0-9\ ]+', '', text)
    return text


def say(*args):
    command = ' '.join(['say'] + list(args))
    if (match('^say[\s]+$', command)):
        return False
    logging.info('executing: {}'.format(command))
    system(command)
    return True


@app.route("/")
def index():
    return "/voices, /say/<text>, /say/<voice>/<text>\n"


@app.route("/voices")
def list_voices():
    command = "say -v '?'"
    logging.info('executing: {}'.format(command))
    return getoutput(command) + "\n"


@app.route("/say/<text>")
def say_text(text='hello'):
    say(sanitize(text))
    return 'ok\n'


@app.route("/say/<voice>/<text>")
def say_voice_text(voice='Alex', text='hello'):
    say('-v', sanitize(voice), sanitize(text))
    return 'ok\n'


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.debug = True
    app.run(debug=False, port=9010, host='0.0.0.0')
