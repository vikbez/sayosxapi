from os import system
from re import escape
from flask import Flask

app = Flask(__name__)

@app.route("/say/<text>")
def say_text(text='hello'):
    system('say %s' % escape(text))
    return 'ok'

@app.route("/say/<voice>/<text>")
def say_voice_text(voice='Alex', text='hello'):
    system('say -v {} {}'.format(escape(voice), escape(text)))
    return 'ok'

if __name__ == "__main__":
    app.run(debug=False, port=9000, host='0.0.0.0')
