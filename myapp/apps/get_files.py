from flask import Blueprint, jsonify, send_file
from settings import BASE_DIR, PHOTO_DIR, MUSIC_DIR
import os

gsa = Blueprint('gsa', __name__)


@gsa.route('/get_photo/<file_name>')
def get_photo(file_name):

    file_path = os.path.join(BASE_DIR, PHOTO_DIR, file_name)

    return send_file(file_path)

@gsa.route('/get_music/<file_name>')
def get_music(file_name):

    file_path = os.path.join(BASE_DIR, MUSIC_DIR, file_name)

    return send_file(file_path)
