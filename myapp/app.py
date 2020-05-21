from flask import Flask, render_template
from apps.content_list import content
from apps.get_files import gsa

app = Flask(__name__)

app.register_blueprint(content)
app.register_blueprint(gsa)


@app.route('/')
def index():
    return 'hello world'


@app.route('/webchat')
def webchat():
    return render_template('wechats.html')


@app.route('/personal')
def personal():
    return render_template('personal.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
