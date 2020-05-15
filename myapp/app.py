from flask import Flask
from apps.content_list import content
from apps.get_files import gsa
app = Flask(__name__)

app.register_blueprint(content)
app.register_blueprint(gsa)

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
