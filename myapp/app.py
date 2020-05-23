from flask import Flask, render_template
from apps.content_list import content
from apps.get_set_files import gsa
from apps.talk import talk
from user import user
from createQR import QR

app = Flask(__name__)

app.register_blueprint(content)
app.register_blueprint(gsa)
app.register_blueprint(talk)
app.register_blueprint(user)
app.register_blueprint(QR)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
