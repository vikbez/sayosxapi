from os import system
from re import escape
from flask import Flask
import logging


app = Flask(__name__)


def say(*args):
    command = ' '.join(['say'] + list(args))
    logging.info('executing: {}'.format(command))
    #system(command)
    return True


@app.route("/say/<text>")
def say_text(text='hello'):
    say(escape(text))
    return 'ok\n'


@app.route("/say/<voice>/<text>")
def say_voice_text(voice='Alex', text='hello'):
    say('-v', escape(voice), escape(text))
    return 'ok\n'


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.debug = True
    app.run(debug=False, port=9000, host='0.0.0.0')
