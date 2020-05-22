from flask import Blueprint, render_template

talk = Blueprint('talk', __name__)


@talk.route('/webchat')
def webchat():
    return render_template('wechats.html')


@talk.route('/personal')
def personal():
    return render_template('personal.html')
