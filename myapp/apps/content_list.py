from flask import Blueprint, jsonify
from settings import client

content = Blueprint('coontent', __name__)


@content.route('/content_list')
def content_list():
    res = list(client['local']['content'].find({}, {"_id": 0}))
    return jsonify(res)


@content.route('/music_list')
def music_list():
    res = list(client['local']['music'].find({}, {"_id": 0}))
    return jsonify(res)
